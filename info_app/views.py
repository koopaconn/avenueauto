from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy,reverse
from django.views.generic import (View,TemplateView,ListView,DetailView)

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class view_repairs(TemplateView):
    template_name = 'info_app/repairs.html'

class view_tires(TemplateView):
    template_name = 'info_app/tires.html'

class view_about(TemplateView):
    template_name = 'info_app/about.html'

class view_signup(TemplateView):
    template_name = 'info_app/signup.html'

class view_carslist(ListView):
    context_object_name = 'car_list'
    model = models.model_cars
    template_name = 'info_app/car_list.html'

class view_cardetails(DetailView):
    context_object_name = 'car_details'
    model = models.model_cars
    template_name = 'info_app/detail.html'
