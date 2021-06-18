from django.db import models
from account.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    tittle = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    comment = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comments')









