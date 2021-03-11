from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(title=title, content=content)
        article.save()
        return redirect('articles:detail', article.pk)
    return render(request, 'articles/form.html')

def detail(request, req_pk):
    article = Article.objects.get(pk=req_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)