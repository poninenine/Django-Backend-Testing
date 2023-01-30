from django import forms
from .models import Image
from django.core.exceptions import ValidationError

class ImageForm(forms.ModelForm):
    
    title = forms.CharField(required=False)
    description = forms.CharField(required=False)
    
    class Meta:
        model = Image
        fields = ('image', 'title', 'description')
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")

        if title == "":
            cleaned_data['title'] = "Default Title"
        
        if description == "":
            cleaned_data['description'] = "Default Description"