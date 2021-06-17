from django.db import models
from account.models import User

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, primary_key=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = (
        ('Published', 'Published'),
        ('Draft', 'Draft')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    tittle = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')
    created = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(Tag)


class Comment(models.Model):
    comment = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comments')









