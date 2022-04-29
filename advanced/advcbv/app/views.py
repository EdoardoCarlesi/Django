from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Simple example
class CBViews(View):
    def get(self, request):
        return HttpResponse('FanCool')

class IndexViews(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injection'] = 'BASIC_INJ'
        return context

