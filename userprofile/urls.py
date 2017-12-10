from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    url(r'^userprofile/$', views.UserProfileList.as_view(), name='profile-list'),
    url(r'^userprofile/(?P<pk>[0-9]+)/$', views.UserProfileDetail.as_view(), name='profile-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
