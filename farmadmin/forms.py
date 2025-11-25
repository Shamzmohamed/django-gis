from django import forms
from .models import Farm, Field

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        exclude = ['last_update', 'last_update_by']

class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        exclude = ['last_update', 'last_update_by']