from datetime import timedelta

import django_filters
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import *

# Create your views here.
from django_filters import FilterSet

from .forms import *
from .models import *
from .permissions import UserHasPermissionMixin


class MainPageView(ListView):
    model = Product
    template_name = 'main.html'
    context_object_name = 'products'


class ProductListView(ListView):
    model = Product
    template_name = 'list_product.html'
    context_object_name = 'products'


# class PostsFilterSet(FilterSet):
#     author = django_filters.CharFilter('author__email', lookup_expr='iexact')
#     created_at = django_filters.DateFilter('created_at', lookup_expr='gt')
#
#     class Meta:
#         model = Post
#         fields = ['tags', 'author']


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.id = kwargs.get('id', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.filter(id=self.id)
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'Category_detail.html'
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(categories=self.slug)
        return context


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company_detail.html'
    context_object_name = 'company'


class AddProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = AddProductForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs

    def get_success_url(self):
        return reverse('product-detail', args=(self.object.id, ))


class AddProductImage(UserHasPermissionMixin, UpdateView):
    model = Product
    template_name = 'add_product_image.html'
    form_class = ImageForm

    def get_success_url(self):
        return reverse('product-detail', args=(self.object.id, ))



def up_image(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.user:
        ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
        formset = ImageFormSet(request.POST or None, request.FILES or None,
                               queryset=Image.objects.filter(product=product))



def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.user:
        ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
        product_form = AddProductForm(request.POST or None, instance=product)
        formset = ImageFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.filter(product=product))
        if product_form.is_valid() and formset.is_valid():
            product_form.save()

            for form in formset:
                image = form.save(commit=False)
                image.product = product
                image.save()
            return redirect(product.get_absolute_url())
        return render(request, 'update_product.html', locals())
    else:
        return HttpResponse('<h1> Error:403 Forbidden</h1>')




# def add_product(request):
#     ImageFormSet = modelformset_factory(Image, form=ImageForm, min_num=2, max_num=5)
#     if request.method == 'POST':
#         product_form = AddProductForm(request.POST)
#         formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
#         if product_form.is_valid() and formset.is_valid():
#             product = product_form.save(commit=False)
#             product.user = request.user
#             product.save()
#             # for k in product_form.cleaned_data['categories']:
#             #     selection = Category.objects.get(slug=k)
#             #     product.category.add(selection)
#
#             # for k in product_form.cleaned_data['categories']:
#             #     p1 = Category.objects.create(name=k)
#             #     p1.save()
#             #     product.category.add(p1)
#
#
#             for form in formset.cleaned_data:
#                 image = form['image']
#                 Image.objects.create(image=image, product=product)
#             return redirect(product.get_absolute_url())
#     else:
#         product_form = AddProductForm()
#         formset = ImageFormSet(queryset=Image.objects.none())
#     return render(request, 'add_product.html', locals())
# #


class DeleteRecipeView(UserHasPermissionMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(request, messages.SUCCESS, 'Successfully deleted!')
        return HttpResponse(success_url)


