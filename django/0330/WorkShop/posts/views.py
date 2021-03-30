from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .forms import PostForm, CommentForm, PickForm
from .models import Post, Comment, Pick


# Create your views here.
@require_safe
def index(request):
    posts = Post.objects.order_by('-pk')
    context = {
        'posts':posts,
    }
    return render(request, 'posts/index.html', context)


@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request, 'posts/create.html', context)


@require_safe
def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    pick = post.pick_set.all()
    comment_form = CommentForm()
    comments = post.comment_set.all()
    context = {
        'post':post,
        'pick':pick,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'posts/detail.html', context)


@require_POST
def create_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.pick.post = post
        comment.save()
        return redirect('posts:detail', post.pk)
    comments = post.comment_set.all()
    context = {
        'post':post,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'posts/detail.html', context)