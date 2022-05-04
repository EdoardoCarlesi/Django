from django.urls import re_path, path
from app import views

app_name='app'

urlpatterns = [
        re_path(r'^$', views.SchoolListView.as_view(), name='list'),
        re_path(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail')
        ]


