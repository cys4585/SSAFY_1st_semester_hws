# 07_WorkShop

### ❖Django Project 

- Django Model Form을 활용해 CRUD를 모두 갖춘 장고 프로젝트를 제작하고 결과 사진과 코드를 별도의 마크다운 파일에 작성하여 제출하시오. 

  

### ❖ 기본 설정 

1) 프로젝트 이름은 crud, 앱 이름은 articles로 설정한다. 

2) 모든 템플릿에서 상속받아 사용할 base.html을 작성한다. base.html이 담긴 templates 디렉토리는 프로젝트 및 앱 디렉토리와 동일한 위치에 생성한다. base.html은 Bootstrap CDN을 포함하고 있어야 한다.



### ❖ CRUD 구현 제시된 결과 사진들을 참고하여 장고 프로젝트를 진행하시오. 

- ```python
  # articles/models.py
  
  from django.db import models
  
  # Create your models here.
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

- ```python
  # articles/forms.py
  
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
  
      class Meta:
          model = Article
          fields = '__all__'
  ```

- ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:pk>/', views.detail, name='detail'),
      path('<int:pk>/update', views.update, name='update'),
      path('<int:pk>/delete', views.delete, name='delete'),
  ]
  ```

- 

1) Read

![image-20210319204048508](07_WorkSHop.assets/image-20210319204048508.png)

- ```python
  # 1) Read
  @require_safe
  def index(request):
      articles = Article.objects.order_by('-pk')
      context = {
          'articles':articles,
      }
      return render(request, 'articles/index.html', context)
  ```

- ```django
  <!-- index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>INDEX PAGE</h1>
    <hr>
    {% for article in articles %}
      <div class="container border">
          <h3>제목 : <a href="{% url 'articles:detail' article.pk %}" >{{ article.title }}</a></h3>
          <p>내용 : {{ article.content }}</p>
      </div>
      <hr>
    {% empty %}
      <p>아직 글이 하나도 없습니다.</p>
    {% endfor %}
  {% endblock content %}
  ```



2) Create

![image-20210319204127244](07_WorkSHop.assets/image-20210319204127244.png)

- ```python
  # 2) Create
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
  ```

- ```django
  <!-- form.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    {% if request.resolver_match.url_name == 'create' %}
      <h1>CREATE PAGE</h1>
    {% elif request.resolver_match.url_name == 'update' %}
      <h1>UPDATE PAGE</h1>
    {% endif %}
    <hr>
    <form action="" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="완료">
    </form>
  {% endblock content %}
  ```



3) Detail

![image-20210319204301871](07_WorkSHop.assets/image-20210319204301871.png)

- ```python
  # 3) Detail
  @require_safe
  def detail(request, pk):
      article = get_object_or_404(Article, pk=pk)
      context = {
          'article': article,
      }
      return render(request, 'articles/detail.html', context)
  ```

- ```django
  <!-- detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>DETAIL PAGE</h1>
    <hr>
    <div class="container border">
        <h3>제목 : {{ article.title }}</h3><br>
        <p>내용 : {{ article.content }}</p>
        <p>작성일 : {{ article.created_at }}</p>
        <p>수정일 : {{ article.updated_at }}</p>
    </div>
    <br>
    <div class="container">
      <form action="{% url 'articles:update' article.pk %}" method="GET">
        {% csrf_token %}
        <input type="submit" value="수정">
      </form>
      <form action="{% url 'articles:delete' article.pk %}" method="POST" style="margin-top:10px">
        {% csrf_token %}
        <input type="submit" value="삭제">
      </form>
    </div>
  {% endblock content %}
  ```



4) Update

![image-20210319204239138](07_WorkSHop.assets/image-20210319204239138.png)

- ```python
  # 4) Update
  @require_http_methods(['POST', 'GET'])
  def update(request, pk):
      article = get_object_or_404(Article, pk=pk)
      if request.method == 'POST':
          form = ArticleForm(request.POST, instance=article)
          if form.is_valid():
              form.save()
              return redirect('articles:detail', pk)
      else:
          form = ArticleForm(instance=article)
      context = {
          'form':form,
      }
      return render(request, 'articles/form.html', context)
  ```

- ```django
  <!-- form.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    {% if request.resolver_match.url_name == 'create' %}
      <h1>CREATE PAGE</h1>
    {% elif request.resolver_match.url_name == 'update' %}
      <h1>UPDATE PAGE</h1>
    {% endif %}
    <hr>
    <form action="" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="완료">
    </form>
  {% endblock content %}
  ```



5) Delete

![image-20210319204407942](07_WorkSHop.assets/image-20210319204407942.png)

- ```python
  # 5) Delete
  @require_POST
  def delete(request, pk):
      article = get_object_or_404(Article, pk=pk)
      article.delete()
      return redirect('articles:index')
  ```

  