from django import forms
from .models import FileObject


class FileObjectAddForm(forms.ModelForm):

    class Meta:
        model = FileObject
        fields = ("input_file", )
