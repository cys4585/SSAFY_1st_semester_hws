# 04_Workshop

![image-20210311194607156](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210311194607156.png)



![image-20210311194634334](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210311194634334.png)



![image-20210311194704773](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210311194704773.png)



![image-20210311194741492](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210311194741492.png)



1. articles/models.py

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

   

2. articles/urls.py

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'articles'
   
   urlpatterns = [
       path('', views.index, name='index'),
       # POST create / GET create 구분됨
       path('new/', views.create, name='create'),
       path('<int:article_pk>/', views.detail, name='detail'),
       path('<int:article_pk>/delete/', views.delete, name='delete'),
       path('<int:article_pk>/edit/', views.update, name='update'),
   ]
   
   ```

   

3. articles/views.py

   ```python
   from django.shortcuts import render, redirect, get_object_or_404
   from .models import Article
   
   # Create your views here.
   def index(request):
       articles = Article.objects.all()
       context = {
           'articles': articles,
       }
       return render(request, 'articles/index.html', context)
   
   def create(request):
       if request.method == 'POST':
           title = request.POST.get('title')
           content = request.POST.get('content')
           article = Article(title=title, content=content)
           article.save()
           return redirect('articles:detail', article.pk)   # GET 방식으로 재요청을 보냄
       else:
           return render(request, 'articles/create.html')
   
   def detail(request, article_pk):
       article = get_object_or_404(Article, pk=article_pk)
       context = {
           'article': article,
       }
       return render(request, 'articles/detail.html', context)
   
   def delete(request, article_pk):
       # article = get_object_or_404(Article, pk=article_pk)
       # if request.method == 'POST':
       #     article.delete()
       #     return redirect('articles:index')
       # return redirect('articles:detail', article.pk)
       article = get_object_or_404(Article, pk=article_pk)
       article.delete()
       return redirect('articles:index')
   
   def update(request, article_pk):
       article = get_object_or_404(Article, pk=article_pk)
       if request.method == 'POST':
           title = request.POST.get('title')
           content = request.POST.get('content')
           article.title = title
           article.content = content
           article.save()
           return redirect('articles:detail', article.pk)
       context = {
           'article':article,
       }
       return render(request, 'articles/update.html', context)
   ```

   

4. templates/base.html

   ```django
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
     <title>Document</title>
   </head>
   <body>
     {% block content %}
     {% endblock content %}
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

   

5. articles/templates/articles/index.html

   ```django
   {% extends 'base.html' %}
   
   {% block content %} 
     <h1>INDEX</h1>
     <a href="{% url 'articles:create' %}">NEW</a><br><br>
       {% for article in articles %}
         <h3>제목 : {{article.title}}</h3>
         <p>내용 : {{article.content}}</p>
         <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
         <hr>
       {% empty %}
         <li> 현재 글이 없습니다.</li>
       {% endfor %}
   {% endblock content %}
   ```

   

6. articles/templates/articles/detail.html

   ```django
   {% extends 'base.html' %}
   {% comment %} django.contrib.humanize {% endcomment %}
   {% load humanize %} 
   
   {% block content %}
     <h1>DETAIL</h1>
     <hr>
     <h3>{{article.title}}</h3>
     <p>{{article.content}}</p>
     <p>작성일 : {{article.created_at}}</p>
     <p>수정일 : {{article.updated_at}}</p>
     {% comment %} <p>{{article.created_at|naturalday}}</p>
     <p>{{article.updated_at|naturaltime}}</p> {% endcomment %}
     <hr>
     {% comment %} <form action="{% url 'articles:delete' article.pk %}" method="POST">
       {% csrf_token %}
       <input type="submit" value="DELETE">
     </form> {% endcomment %}
     <a href="{% url 'articles:update' article.pk %}">EDIT</a>
     <a href="{% url 'articles:delete' article.pk %}">DELETE</a><br>
     <a href="{% url 'articles:index' %}">BACK</a>
   {% endblock content %}
   ```

   

7. articles/templates/articles/create.html

   ```django
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>NEW</h1>
     <hr>
     <form action="" method="POST">
       {% csrf_token %}
       <label for="title">TITLE : </label>
       <input type="text" id="title" name="title"><br>
       
       <label for="content">CONTENT : </label>
       <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
   
       <input type="submit" value="작성">
     </form>
     <a href="{% url 'articles:index' %}">BACK</a>
   {% endblock content %}
   ```

   

8. articles/templates/articles/update.html

   ```django
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>NEW</h1>
     <hr>
     <form action="" method="POST">
       {% csrf_token %}
       <label for="title">TITLE : </label>
       <input type="text" id="title" name="title" value="{{article.title}}">
       <br>
       
       <label for="content">CONTENT : </label>
       <textarea name="content" id="content" cols="30" rows="10">{{article.content}}</textarea>
       <br>
   
       <input type="submit" value="작성">
     </form>
     <a href="{% url 'articles:index' %}">BACK</a>
   {% endblock content %}
   ```

   

