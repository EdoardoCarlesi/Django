from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from app import models


class IndexView(TemplateView):
    template_name = 'app/index.html'

class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School
    
class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('app:list')
