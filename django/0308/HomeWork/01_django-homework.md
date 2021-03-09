# 01_HomeWork

### 1. 한국 시간 나타내기

1-1. django 서버를 실행하고 첫 페이지에 접속했을 때 터미널에 출력된 서버 시간이 현재 한국 시간과 다른 시간으로 출력된다. 이를 한국 시간으로 바꾸려면 settings.py에 어떤 변 수 그리고 어떤 값을 할당해야 하는지 작성하시오. 

```python
TIME-ZONE = 'Asia/Seoul'
```



1-2. 추가로 settings.py에 "이 변수"가 False인 상태로 1-1번 변수를 설정하는 것은 error라 고 한다. "이 변수"는 무엇인가?

```python
USE_TZ
```



### 2. 경로 설정하기

다음은 어떤 django 프로젝트의 urls.py의 모습이다. 주소 ’/ssafy’로 요청이 들어왔을 때 실행되는 함수가 pages 앱의 views.py 파일 안 ssafy 함수라면, 요청에 응답하기 위해 빈칸 __(a)__에 추가되어야 할 코드를 작성하시오.

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path(___(a)___),
    path('admin/', admin.site.urls),
]
```

```python
'ssafy/', views.ssafy
```



### 3. Django Template Language

아래 링크를 참고하여 각 문제들을 해결하기 위한 코드를 작성하시오. 

https://docs.djangoproject.com/en/3.1/ref/templates/builtins/



1) menus 리스트를 반복문으로 출력하시오.

```django
{% for menu in menus %}
	<p>{{ menu }} </p>
{% endfor %}
```

2) posts 리스트를 반목문을 활용하여 0번 글부터 출력하시오.

```django
{% for post in posts %}
	<p>{%{% {{forloop.counter0}}번 글 : {{ post }} %}</p>
{% endfor %}
```

3) users 리스트가 비어있다면 현재 가입한 유저가 없습니다. 텍스트를 출력하시오.

```django
{% for user in users %}
	<p>{{user}}</p>
{% empty %} <p>현재 가입한 유저가 없습니다.</p>
{% endfor %}
```

4) 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리 하시오.

```django
{% if forloop.first %}
	<p>첫 번째 반복문 입니다.</p>
{% else %}
	<p>첫 번째 반복문이 아닙니다.</p>
{% endif %}
```

5) 출력된 결과가 주석과 같아지도록 하시오.

```django
<!-- 5 -->
<p>{{ 'hello'|length }}</p>
<!-- My Name Is Tom -->
<p>{{ 'my name is tom'|title }}</p>
```

6) 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 하시오.

```django
<!-- 2020년 02월 02일 (Sun) PM 02:02 -->
{{ today|date:"Y년 m월 d일 (D) A h:i"}}
```



### 4. Form tag with Django

다음은 form tag에 관한 문제이다. 올바른 답을 작성하시오.

```html
<form action="/create/" method="">
    <label for="title">Title : </label>
    <input type="text" name="title" id="title">
    <label for="content">Content : </label>
    <input type="text" name="content" id="content">
    <label for="my-site">My-Site : </label>
    <input type="text" name="my-site" id="my-site">
    <input type="submit">
</form>
```

1) 지문의 코드 중 form 태그의 속성인 action의 역할에 대해 설명하시오. 

- submit을 했을 때 요청할 url

2) 지문의 코드 중 method가 가질 수 있는 속성 값을 작성하시오. 

- GET, POST

3) input 태그에 각각 `안녕하세요`, `반갑습니다`, `파이팅` 문자열을 넣고 submit 버튼을 눌렀을 때 이동하는 url 경로를 작성하시오.

- /localhost:8000/create/?title=안녕하세요&content=반갑습니다&my-site=파이팅

