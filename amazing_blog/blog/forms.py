from models import Post
from django import forms
from django.core.validators import MinLengthValidator

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
