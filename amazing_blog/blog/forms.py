from models import Post
from django import forms
from django.core.validators import MinLengthValidator

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class PostForm(forms.ModelForm):
    mas = forms.CharField(
            widget = forms.Textarea(
                attrs={'cols': 80, 
                       'rows': 20}
                ),
            required = False,
            validators = [MinLengthValidator(20)]
            )

    class Meta:
        model = Post
