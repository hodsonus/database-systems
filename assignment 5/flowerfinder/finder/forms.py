from django import forms
from .models import Flowers

class FlowerSelectForm(forms.Form):
    flowers = forms.ChoiceField(choices=[(flower.comname, flower.comname) for flower in Flowers.objects.raw('SELECT * FROM flowers where comname like "%"')], \
                                widget=forms.Select(attrs={'onchange': 'onSelectFormChange(this.options[this.selectedIndex].value);'}))

class FlowerInformationForm(forms.Form):
    genus = forms.CharField(label='Genus', required=True, max_length=30)
    species = forms.CharField(label='Species', required=True, max_length=30)

class NewSightingForm(forms.Form):
    person = forms.CharField(label='Person', required=True, max_length=30)
    location = forms.CharField(label='Location', required=True, max_length=30)
    sighted = forms.DateField(label='Sighted', input_formats=['%d-%m-%Y'], required=True)