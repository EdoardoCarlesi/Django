from django.urls import path, re_path
from app import views

# Template tagging
app_name = 'app'

urlpatterns = [
        path(r'^$', views.index, name='index'),
        re_path(r'^relative_url/$', views.relative_url, name='relative_url'),
        re_path(r'^other/$', views.other, name='other'),
        ]

