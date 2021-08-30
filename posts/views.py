# Standard libraries
import pdb # Python debugger

# Django Core
from django.shortcuts import render
from django.http import HttpResponse, response, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from posts.models import Post

# Exception
from django.db.utils import IntegrityError

# Utilities
import json
from datetime import datetime

# Forms
from posts.forms import PostForm

# Create your views here.

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.hTml'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed') # don't evaluate until needed

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

def list_posts_deleted(request):
    content = []
    for post in posts:
        content.append(f"""
            <p><strong>{post['name']}</strong></p>
            <p><small>{post['user']} - <i>{post['timestamp']}</i></small></p>
            <figure><img src="{post['picture']}"/></figure>
        """)
    return HttpResponse('<br>'.join(content))

def list_posts_test(request):
    posts = ['a', 'b', 'c']
    result = {
        'posts': posts,
    }
    return JsonResponse(result, safe=True)

    # posts = ['a', 'b', 'c']
    # return JsonResponse(posts, safe=False)
    
def template_testing(request):
    # return render(request, 'feed.html', {'context': 'ViewContext testing', 'posts': posts})
    return render(request, 'posts/feed.html', {'context': 'ViewContext testing', 'posts': posts})

# @login_required
# def list_posts(request):
#     # return render(request, 'feed.html', {'context': 'ViewContext testing', 'posts': posts})
#     return render(request, 'posts/feed.html', {'context': 'ViewContext testing', 'posts': posts})

@login_required
def list_posts(request):
    """List existing posts."""
    posts = Post.objects.all().order_by('-created')

    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )