from .models import TempData
from django import forms
from django.contrib.admin import widgets
from django.forms.widgets import MultiWidget
        
class InputForm(forms.ModelForm):
    date_time = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    
    class Meta:
        model = TempData
        fields = ['temp','date_time']