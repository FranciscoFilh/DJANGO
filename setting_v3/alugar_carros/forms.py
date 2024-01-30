from django import forms
from .models import AlugarCarro

class AlugarCarroForm(forms.ModelForm):
    class Meta:
        model = AlugarCarro
        fields = '__all__'