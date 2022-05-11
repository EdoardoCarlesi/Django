from django.urls import re_path
from blog import views


urlpatterns = [
        re_path(r'^about/$', views.AboutView.as_view(),name='about'),
        
        ]

