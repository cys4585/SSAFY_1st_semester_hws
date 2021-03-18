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



