# 03_workshop

![image-20210311183352327](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210311183352327.png)

![image-20210311183409760](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210311183409760.png)

![image-20210311183434637](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210311183434637.png)



1. articles/urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create, name='create'),
    path('<int:req_pk>/detail/', views.detail, name='detail'),
]

```



1. articles/views.py

```python
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
```



1. articles/moels.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



1. articles/templates/articles/detail.html

```django
{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <p>글 번호 : {{article.pk}}</p>
  <p>제목 : {{article.title}}</p>
  <p>내용 : {{article.content}}</p>
  <p>최초 작성 시간 : {{article.created_at}}</p>
  <p>최근 수정 시간 : {{article.updated_at}}</p>
  <a href="{% url 'articles:index' %}">[BACK]</a>
{% endblock content %}
```



1. articles/templates/articles/form.html

```django
{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="" method="POST">
    {% csrf_token %}
    <label for="title">TITLE: </label>
    <input type="text" id="title" name="title"><br>

    <label for="content">CONTENT: </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea><br>

    <input type="submit" value="작성">
  </form>

  <a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}
```



1. articles/templates/articles/index.html

```django
{% extends 'base.html' %}

{% block content %}
  <h1>INDEX</h1>
  <a href="{% url 'articles:create' %}">NEW</a><br><br>

  {% for article in articles %}
    <h3>제목: {{article.title}}</h3>
    <p>내용: {{article.content}}</p>
    <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
    <hr>
  {% empty %}
    <p>게시글이 하나도 없습니다.</p>
  {% endfor %}
{% endblock content %}
```

