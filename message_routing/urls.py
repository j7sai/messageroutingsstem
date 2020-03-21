from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^gateway/(?P<id>[0-9]*)/*$',views.gatewayview),
    url(r'^route/(?P<id>[0-9]*)/*$',views.RouterView.as_view()),
    url(r'search/route/(?P<id>\+*[0-9]+)/',views.RouterSearchView.as_view())
]