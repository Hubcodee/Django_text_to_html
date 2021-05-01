from django import forms
from .models import text_to_html

from django_summernote.admin import SummernoteModelAdmin

class T2HtmlForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(),label="Text Editor")

    class Meta:
        model = text_to_html
        fields = '__all__'