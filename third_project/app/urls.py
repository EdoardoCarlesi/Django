from django.urls import re_path, path
from app import views


urlpatterns = [
        re_path(r'^$', views.users, name='users'),
        ]
