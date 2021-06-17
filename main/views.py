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


class MainView(ListView):
    model = Post
    template_name = 'main.html'
    context_object_name = 'posts'


class AccountDetailView(DetailView):
    model = User
    template_name = 'account_detail.html'
    context_object_name = 'user'


