from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
# from django.urls import path,include
urlpatterns = [
    url(r'', include(('message_routing.urls','message_routing'), namespace='message_routing')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
