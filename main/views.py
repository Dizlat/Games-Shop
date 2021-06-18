from datetime import timedelta

import django_filters
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
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
from .permissions import UserHasPerMixin


class MainView(ListView):
    model = Post
    template_name = 'main.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class AccountDetailView(DetailView):
    model = User
    template_name = 'account_detail.html'
    context_object_name = 'user'


class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = AddPostForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse('post-detail', args=(self.object.id, ))


class UpdatePostView(UserHasPerMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = UpdatePostForm

    def get_success_url(self):
        return reverse('post-detail', args=(self.object.id, ))


class DeletePostView(UserHasPerMixin, DeleteView):
    model = Post
    template_name = 'post-delete.html'
    success_url = reverse_lazy('home')


class SearchResultView(View):
    def get(self, request):

        q = request.GET.get('query', '')
        print()
        print(request)
        print()
        print()
        print()

        if q:
            posts = Post.objects.filter(
                Q(tittle__icontains=q) |
                Q(description__icontains=q)
            )
        else:
            posts = Post.objects.none()
        return render(request, 'main.html', {'posts': posts})
