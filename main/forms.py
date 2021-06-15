from ckeditor import widgets
from django import forms
from .models import Product, Image


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['title', 'text', 'image', 'category', 'tags']


class ImageForm(forms.ModelForm):
    photos = forms.FileField(widget=widgets.FileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        super(ImageForm, self).__init__(*args, **kwargs)

    def clean_photos(self):
        images = [image for image in self.request.FILES.getlist('images') if 'image' in image.content_type]
        # Если среди загруженных файлов картинок нет, то исключение
        if len(images) == 0:
            raise forms.ValidationError(u'Not found uploaded images.')
        return images

    def save_for(self, product):
        for image in self.cleaned_data['photos']:
            ImageForm(image=image, product=product).save()

