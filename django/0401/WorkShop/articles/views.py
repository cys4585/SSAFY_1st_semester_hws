from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.http import HttpResponse, HttpResponseForbidden
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # hashtag
            # content = Text ...
            # content를 공백 기준으로 리스트로 만든다.
            for word in article.content.split(): # => ['content', '#hash', '#tag']
                # #으로 시작하는 문자들만 뺀다. -> startswith
                if word.startswith('#'):
                    print(word)
                    # 그렇게 걸러온 word를 생성할 것이다.
                    # 생성 혹은 조회
                    # 반환되는 값은 (Object, Boolean)
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    print(hashtag, created)
                    # article과 hashtag의 M:N 관계 형성 
                    article.hashtags.add(hashtag)
                    print('*'*30)
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                # hashtag
                # article이 관계되어 있는 모든 hash와의 연결 끊기.
                article.hashtags.clear()
                for word in article.content.split():
                    if word.startswith('#'):
                        hashtag, created = Hashtag.objects.get_or_create(content=word)
                        article.hashtags.add(hashtag)
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
        # return HttpResponseForbidden()
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
        

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')
    # return HttpResponse(status=401)


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        # return HttpResponseForbidden()
    return redirect('articles:detail', article_pk)
    # return HttpResponse(status=401)


@require_POST
def like(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')


@login_required
def hashtag(request, hash_pk):
    # 이 해시태그가 무엇인지
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    # 이 해시태그와 관계 맺고 있는 articles 전부
    articles = hashtag.article_set.all()
    context = {
        'hashtag': hashtag,
        'articles': articles,
    }
    return render(request, 'articles/hashtag.html', context)