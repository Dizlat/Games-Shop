from django.db import models
from account.models import User

# Create your models here.


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name

    def get_children(self):
        if self.children:
            return self.children.all()
        return False


class Tag(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    release_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.tittle


class Company(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos')
    description = models.TextField()
    product = models.ForeignKey(Product, related_name='company-products')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    rate = models.RatingField(range=5)
    created = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.url




