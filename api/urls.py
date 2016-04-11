from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from api.views import GetKeyView, RepayKeyView, KeyStatusView, KeyInfoView


urlpatterns = [
    url(r'getkey/', GetKeyView.as_view()),
    url(r'repay/', csrf_exempt(RepayKeyView.as_view())),
    url(r'status/', KeyStatusView.as_view()),
    url(r'info/', KeyInfoView.as_view()),
]
