# 10_HomeWork

### 1. Lookup

- 지문의 코드에서 ‘__gt’ 부분을 lookup이라고 한다. 링크를 참고하여 Django에서 사용 가능 한 lookup 세가지와 그 의미를 작성하시오. 

  https://docs.djangoproject.com/en/3.1/ref/models/querysets/#field-lookups

  ```python
  Entry.objects.filter(pk__gt=4)
  ```
  
  - gt : Greater Than
  - gte : Greater Than or Equal to
  - lt : Less Than
  - lte : Less Than or Equal to
  - startswith



### 2. 1:N 관계 설정

- 지문은 1:N 관계 설정을 하기 위하여 정의된 모델이다. 링크를 참고하여 빈 칸에 들어갈 수 있는 값 세가지를 선택 후 그 의미를 작성하시오. 

  https://docs.djangoproject.com/en/3.1/ref/models/fields/#arguments

  ```python
  class Comment(models.Model):
      content = models.CharField(max_length=100)
      article = models.ForeignKey(Article, on_delete=__(a)__)
  ```

  - CASCADE : 부모 객체(참조된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제됨
  - PROTECT : 참조가 되어 있는 경우 오류 발생
  - SET_NULL : 부모 객체가 삭제됐을 때 모든 값을 NULL로 치환
  - SET_DEFAULT : 모든 값이 DEFAULT 값으로 치환
  - SET() : 특정 함수 호출
  - DO_NOTHING : 아무것도 하지 않음
    - 다만, 데이터베이스 필드에 대한 SQL ON DELETE 제한 조건을 설정해야 함



### 3. comment create view 

- 지문은 댓글 기능을 작성하기 위한 코드이다. 빈 칸에 들어갈 코드와 의미를 작성하시오.

  ```python
  def comment_create(request, pk):
      Article = Article.objects.get(pk=pk)
      if request.method == 'POST':
          form = CommentForm(request.POST)
          if form.is_valid():
              comment = form.save(__(a)__)
              comment.article = article
              comment.save()
             	return redirect('atciels:index')
  ```

  - commit=False
    - save(객체생성)는 하지만, commit(DB의 table에 저장)하지는 않는다.



### 4. 1:N DB API 

- 게시물 아래에 댓글을 출력하려고 한다. Article과 Comment 모델이 1:N으로 관계설정 이 되어 있다고 가정 할 때 아래의 빈칸에 적절한 코드를 작성하시오.

  ```html
  <h1>{{ article.title }}</h1>
  {% for comment in __(a)__ %}
    <p>{{ comment.content }}</p>
  {% empty %}
    <p>댓글이 없습니다.</p>
  {% endfor %}
  ```

  - article.comment_set.all

