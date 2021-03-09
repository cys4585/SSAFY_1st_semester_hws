### 02_HomeWork

#### 1. MTV 

Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의 약자이며 각각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 django에서 하는 역할을 간략히 서술하시오.

- M : Model - Model - 데이터 작업

- T : Template - View - 응답할 때 보여줄 모습

- V :  View - Controller - 요청에 맞는 응답을 위한 작업

  

#### 2. URL 

`__(a)__`는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을 의미한다. `__(a)__`는 무엇인지 작성하시오.

- Variable Routing

  

#### 3. Django template path 

Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴더 안의 __(a)__ 폴더 내부를 탐색한다. __(a)__에 들어갈 폴더 이름을 작성하시오.

- templates



#### 4. Static web and Dynamic web 

Static web page와 Dynamic web page의 특징을 간단하게 서술하시오.

- Static web page 
  - 서버에 저장된 파일이 그대로 전달된다.
  - 서버는 사용자의 요청에 해당하는 페이지를 그대로 전달한다.
  - 사용자는 서버의 데이터가 변경되지 않는 이상 늘 고정된 웹 페이지를 본다.
- Dynamic web page
  - 서버에 있는 데이터들을 스크립트에 의해 가공처리 후 생성된 페이지를 전달한다.
  - 서버는 사용자의 요청을 해석한 후 가공된 페이지를 전달한다.
  - 사용자는 특정한 상황이거나 시간 및 요청에 따라 달라지는 웹 페이지를 본다.