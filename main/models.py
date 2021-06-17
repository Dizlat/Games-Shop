from django.db import models
from account.models import User

# Create your models here.


class Company(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos')
    description = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):

    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name

    def get_children(self):
        if self.children:
            return self.children.all()
        return False


class Product(models.Model):
    tittle = models.CharField(max_length=250)
    description = models.TextField()
    system_requiremenrs = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    company = models.ForeignKey(Company, models.DO_NOTHING, related_name='products')

    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.tittle

    @property
    def get_image(self):
        return self.images.first()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product-detail', kwargs={'pk': self.pk})



class Review(models.Model):
    text = models.TextField()
    # rate = models.RatingField(range=5)
    created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='reviews')


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.url







