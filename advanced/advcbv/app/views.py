from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from app import models


class SchoolView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'app/school.html'

