
from django import forms

from .models import Product, Image


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['title', 'text', 'image', 'category', 'tags']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

