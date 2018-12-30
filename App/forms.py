from django import forms

from .models import TStat14



class SelectProvincesForm(forms.Form):

    provinces = forms.ModelChoiceField(TStat14.objects.all())
