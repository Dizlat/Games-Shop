from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, DeleteView, CreateView

# Create your views here.
from .forms import *
from .models import *


class MainPageView(ListView):
    model = Product
    template_name = 'main.html'
    context_object_name = 'products'


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category_id=self.slug)
        return context


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company_detail.html'
    context_object_name = 'company'


class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag-detail.html'
    context_object_name = 'tag'




# class AddProduct(CreateView):
#     model = Product
#     template_name = 'add_product.html'
#     form_class = AddProductForm
#
#     def get_success_url(self):
#         return reverse('product-detail', args=(self.object.id, ))


# class AddImage(CreateView):
#     model = Image
#     template_name = 'add_product.html'
#     form_class = ImageForm


# def add_product(request):
#     ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
#     if request.method == 'POST':
#         product_form = AddProductForm(request.POST)
#         formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
#         if product_form.is_valid() and formset.is_valid():
#             recipe = product_form.save(commit=False)
#             # recipe.user = request.user
#             recipe.save()
#
#             for form in formset.cleaned_data:
#                 image = form['image']
#                 Image.objects.create(image=image, recipe=recipe)
#             return redirect(recipe.get_absolute_url())
#     else:
#         product_form = AddProductForm()
#         formset = ImageFormSet(queryset=Image.objects.none())
#     return render(request, 'add_product.html', locals())



