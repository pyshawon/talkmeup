from django.conf.urls import url

from . import views

app_name = 'uploads'
urlpatterns = [
    url(r'^$', views.upload, name='upload')
]
