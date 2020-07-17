from django.forms import ModelForm
from .models import Note


class AddNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['content']
