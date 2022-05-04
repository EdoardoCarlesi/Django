from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from app import models

class IndexView(TemplateView):
    template_name = 'app/index.html'

class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
