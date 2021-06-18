from datetime import timedelta
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import *

from .forms import *
from .models import *
from .permissions import UserHasPerMixin


class MainView(ListView):
    model = Post
    template_name = 'main.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostListView(ListView):
    model = Post
    template_name = 'search.html'

    def get_template_names(self):
        template_name = super(PostListView, self).get_template_names()
        search = self.request.GET.get('q')
        filter = self.request.GET.get('filter')
        if search:
            template_name = 'search.html'
        elif filter:
            template_name = 'new.html'
        return template_name

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('q')
        filter = self.request.GET.get('filter')
        if search:
            context['posts'] = Post.objects.filter(Q(tittle__icontains=search) |
                                                    Q(description__icontains=search))
        elif filter:
            start_date = timezone.now() - timedelta(days=1)
            context['posts'] = Post.objects.filter(created__gte=start_date)
        else:
            context['posts'] = Post.objects.all()
        return context


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


class CommentPostView(UserHasPerMixin, CreateView):
    model = Comment
    template_name = 'post_detail.html'
    form_class = CommentForm
#
#     def get_success_url(self):
#         return reverse('post-detail', args=(self.object.id, ))



