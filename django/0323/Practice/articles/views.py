from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .forms import ArticleForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/form.html', context)


@require_safe
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)


@require_http_methods(['POST', 'GET'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        pass
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/form.html', context)