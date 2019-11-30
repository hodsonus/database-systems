from django import forms
from .models import Flowers

class FlowerForm(forms.Form):
    flowers = forms.ChoiceField(choices=[(flower.comname, flower.comname) for flower in Flowers.objects.raw('SELECT * FROM flowers where comname like "%"')], \
                                widget=forms.Select(attrs={'onchange': 'fillTableOnChange(this.options[this.selectedIndex].value);'}))

    def get(self):
        print('FlowerForm: I made it !')