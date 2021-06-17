
from django import forms

from .models import Product, Image, Category


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('user',)

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(AddProductForm, self).__init__(*args, **kwargs)

    def save(self):
        data = self.cleaned_data
        data['user'] = self.request.user
        categories = data.pop('categories')
        product = Product.objects.create(**data)
        product.categories.add(*categories)
        return product


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

