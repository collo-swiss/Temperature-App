from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TempData

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'all_data'
    
    def get_queryset(self):
        return TempData.objects.all
    
"""class InputView(generic.FormView):
    model = TempData
    template_name = 'input.html'"""
    
class RecordTemp(CreateView):
    model = TempData
    fields = ['temp', 'date_time']
    
def input(request):
    return render(request, 'input.html')