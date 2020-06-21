from django import forms
from .models import Ticket


class AddForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'type', 'description']
