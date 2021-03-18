# 06_HomeWork

### 1. Compiled Bootstrap CSS, JS 파일을 다운로드 받아 Django 프로젝트에 Static 파일로 추가하시오.

![image-20210318125351754](06_HomeWork.assets/image-20210318125351754.png)

![image-20210318125404586](06_HomeWork.assets/image-20210318125404586.png)

1. project 폴더 밑에 static 폴더 생성, static 폴더 밑에 css, js 폴더 생성, 각 폴더 밑에 bootstrap css, js파일 생성

2. project의 settings.py 에 아래와 같이 앱에서  static 파일을 찾을 경로를 추가해놓는다...? 

   ```python
   STATICFILES_DIRS = [
       BASE_DIR / projectname / 'static'
   ]
   ```

3. static 파일로 추가한 bootstrap css, js 쓰는 법

   1. 프로젝트 내의 베이스 템플릿에서 부르는 법

      ```django
      <!-- base.html -->
      
      {% load static %}
      
      ...
      
      <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
      
      ...
      
      <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
      ```

      

   2. 앱의 템플릿에서 부르는 법

      - 베이스 템플릿에 블록을 만든다.

        ```django
        <!-- base.html -->
        
        ...
        
        {% block bootstrapcss %}
        {% endblock bootstrapcss %}
        
        ...
        
        {% block bootstrapjs %}
        {% endblock bootstrapjs %}
        ```

      - 앱의 탬플릿에서 블록에 static 파일을 로드한다.

        ```django
        <!-- index.html -->
        {% load static %}
        
        ...
        
        {% block bootstrapcss %}
        	<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
        {% endblock bootstrapcss %}
        
        ...
        
        {% block bootstrapjs %}
        	<script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
        {% endblock bootstrapjs %}
        ```

- 뇌피셜 : 브라우저는 효율성을 위해 이전의 데이터들..? 을 캐싱해 놓는다. 그래서 가끔 개발할 때 어떤 내용을 수정(삭제or추가)해도 브라우저에 안먹히는 경우가 있을 수 있다.????????????????????????????
- memory cache

- 캐싱의 역할
  - 파일을 한번 받아오면, 브라우저에 임시로 저장한다.
  - 이유 : 페이지를 불러올 때마다 파일을 불러오면 비효율적이기 때문
  - 페이지를 처음 불러올 때 파일을 memory cache에 임시로 저장해놓고 다시 로드될 때는 이 memory cache에 저장되어 있는 파일을 사용한다. -> 훨씬 효율적이다.

