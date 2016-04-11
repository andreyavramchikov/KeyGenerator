from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from django.views.generic.base import View

from api.models import UserKey, Key


class GetKeyView(View):

    """
    If we agreed that all keys in systems are predefined then we use our DB
    at first glance I thought that I must generate unique key on the fly,
    rather than get it  from storage
    """
    def get_key(self):
        key = Key.objects.filter(status=Key.NOT_ISSUED).first()
        key.status = Key.ISSUED
        key.save()
        return key

    def get(self, *args, **kwargs):
        request = self.request
        if not request.session.session_key:
            request.session.save()
        session_key = request.session.session_key
        key = self.get_key()
        try:
            UserKey.objects.create(key=key, session=session_key)
        except IntegrityError:
            pass
        return JsonResponse({'key': key.value})


class RepayKeyView(View):

    def post(self, *args, **kwargs):
        key_value = self.request.POST.get('key')
        session = self.request.session.session_key

        try:
            key = Key.objects.get(value=key_value)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'There is no such key - {} '.format(key_value)}, status=200)

        user_key = UserKey.objects.filter(key=key).first()
        if user_key and user_key.session != session:
            return JsonResponse({'message': 'You are not allow to repay this key'}, status=403)

        if user_key and user_key.session == session:
            if key.status == Key.ISSUED:
                key.status = Key.REPAID
                key.save()
                return JsonResponse({'message': 'The key - {} has been repaid'.format(key)}, status=200)
            else:
                return JsonResponse({'message': 'The key - {} already repaid'.format(key)}, status=200)


class KeyStatusView(View):

    def get(self, *args, **kwargs):
        key = self.request.GET.get('key')
        try:
            key = Key.objects.get(value=key)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'No such key in system'})

        return JsonResponse({'status': 'Key status is {}'.format(key.status)})


class KeyInfoView(View):

    def get(self, *args, **kwargs):
        return JsonResponse({'status': 'Amount of not issued keys: {}'.format(
            Key.objects.filter(status=Key.NOT_ISSUED).count())})
