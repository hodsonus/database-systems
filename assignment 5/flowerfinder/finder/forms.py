from django import forms
from .models import Flowers, Features

class FlowerSelectForm(forms.Form):
    flowers = forms.ChoiceField(
        choices = [(flower.comname, flower.comname) for flower in Flowers.objects.raw('SELECT * FROM flowers where comname like "%"')],
        widget = forms.Select(attrs={'onchange': 'onSelectFormChange(this.options[this.selectedIndex].value);'}))

class FlowerInformationForm(forms.Form):
    genus = forms.CharField(label='Genus', required=True, max_length=30)
    species = forms.CharField(label='Species', required=True, max_length=30)

class NewSightingForm(forms.Form):
    person = forms.CharField(label='Person', required=True, max_length=30)
    location = forms.ChoiceField(
        choices = [(feature.location, feature.location) for feature in Features.objects.raw('SELECT * FROM FEATURES where location like "%"')],
        widget = forms.Select()
    )
    sighted = forms.DateField(
        label = 'Sighted',
        widget = forms.SelectDateWidget,
        input_formats = ('%m/%d/%Y', )
    )
