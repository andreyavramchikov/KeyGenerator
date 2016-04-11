from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from api.views import GetKeyView, RepayKeyView, KeyStatusView, KeyInfoView


urlpatterns = [
    url(r'getkey', GetKeyView.as_view()),
    url(r'repaykey', csrf_exempt(RepayKeyView.as_view())),
    url(r'keystatus', KeyStatusView.as_view()),
    url(r'keyinfo', KeyInfoView.as_view()),
]
