from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import texthtmlformatter


class T2HtmlForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(),label="Text Editor")

    class Meta:
        model = texthtmlformatter
        fields = '__all__'