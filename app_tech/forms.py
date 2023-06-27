from django import forms
from django.forms import ModelForm
from .models import *
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('client', 'date', 'products')
        labels = {
            'client': 'client',
            'date':'date',
            'products':'products',
        }
        widgets = {
            'client': forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.DateInput(attrs={'class':'form-control'}),
            'products':forms.TextInput(attrs={'class':'form-control'}),
        }