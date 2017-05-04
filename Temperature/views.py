from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TempData
from .forms import InputForm
from django.contrib.admin import widgets
from django import forms
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'all_data'
    
    def get_queryset(self):
        return TempData.objects.all
    
    
class RecordTemp(CreateView):
    template_name = 'input.html'
    model = TempData
    form_class = InputForm
    success_url = reverse_lazy('Temperature:index')
    

    
