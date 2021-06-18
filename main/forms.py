from django import forms

from .models import *


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['tittle', 'description', 'image', 'tags']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(AddPostForm, self).__init__(*args, **kwargs)

    def save(self):
        data = self.cleaned_data
        data['user'] = self.request.user
        tags = data.pop('tags')
        post = Post.objects.create(**data)
        post.tags.add(*tags)
        return post


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['tittle', 'description', 'image', 'tags']




