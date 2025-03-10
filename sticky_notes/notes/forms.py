from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    A form for creating and updating Note instances.

    This form is based on the Note model and includes fields
    for 'title' and 'content'. It automatically generates
    form fields based on the model definition.
    """

    class Meta:
        model = Note
        fields = ["title", "content"]
