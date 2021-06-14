from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, DeleteView, CreateView

# Create your views here.
from .models import *


class MainPageView(ListView):
    model = Product
    template_name = 'main.html'
    context_object_name = 'products'


class ProductView(ListView):
    pass
