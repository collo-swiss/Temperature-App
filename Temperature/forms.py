from .models import TempData
from django import forms
from django.contrib.admin import widgets

"""class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']"""
        
class InputForm(forms.ModelForm):
    date_time = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    
    class Meta:
        model = TempData
        fields = ['temp','date_time']