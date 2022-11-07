from django import forms

from . import models


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ('image', 'caption', 'alt_text',)
        help_text = {
            'alt_text': 'Should not be more than 125 characters.',
        }