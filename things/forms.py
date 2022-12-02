"""Forms of the project."""

# Create your forms here.

from django import forms
from .models import User

class ThingForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name']


        label = 'Quantity'
        widgets = { 'quantity':forms.NumberInput() }
        validators=[RegexValidator(
            regex=r'^(?=.*[0-9]).*$',
            message='Quantity must be a number.'

        label2 = 'Description'
        widgets = { 'Description':forms.Textarea() }
     )]
