from django.urls import re_path, path
from second_app import views


urlpatterns = [
        re_path(r'^$', views.help, name='help')
        ]
