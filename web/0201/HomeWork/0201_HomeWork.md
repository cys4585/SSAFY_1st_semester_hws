# 0201_HomeWork

### 1. HTML 정의

- 아래의 보기 (1) ~ (4) 중에서, HTML의 본딧말을 고르시오. 

  (1) Hyperlinks and Text Markup Language 

  (2) Home Tool Markup Language 

  **(3) Hyper Text Markup Language **

  (4) Hyper Tool Markup Language

  

### 2. HTML 개념

- 각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오

  1) 웹 표준을 만드는 곳은 Mozilla 재단이다. 

  	- **F** - 웹 표준을 만드는 곳은 w3c(전통적) / WHATWG(현대적)

  2) 표(table) 을 만들 때에는 반드시  <th> 태그를 사용해야 한다. 

  	- **F** - 표를 만들때 반드시 th 라는 태그를 사용할 필요는 없다.

  3) 제목(Heading) 태그는 제목 이외에는 사용하지 않는 것이 좋다. 

  	- **T** - 시멘틱 태그들은 그 의미에 맞게 사용하는 것이 옳다.

  4) 리스트를 나열하기 위해서는 <ul> 태그만 사용 할 수 있다.

  	- **F** -  ul, ol 태그가 있으며, 각각의 요소들은 li태그로 작성한다.

  5) HTML의 태그는 반드시 별도의 닫는 태그가 필요하다.

  	- **F** - 여는 태그와 닫는 태그가 한 쌍인 태그도 있고, 별도로 닫는 태그가 필요하지 않은 self-closing 태그가 있다.

  

### 3. CSS 정의

- 아래의 보기 (1) ~ (4) 중에서, CSS의 본딧말을 고르시오. 

  (1) Creative Style Sheets 

  **(2) Cascading Style Sheets **

  (3) Computer Style Sheets 

  (4) Colorful Style Sheets



### 4. CSS 개념

 - 각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오.

   1) HTML과 CSS는 각자 문법을 갖는 별개의 언어이다. 

   	- **T** - CSS는 HTML이 없으면 작동할 수 없지만, 두개는 명확히 별개의 언어이다.

   2) 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다.

   - **T** - 웹 브라우저별로 내장 기본 스타일이 존재한다.

   3) 자식 요소 프로퍼티는 부모의 프로퍼티를 모두 상속 받는다. 

   - **F** - 모든 속성을 상속받지는 않는다.
     - 대표적인 속성으로 width, height, background-color 등은 상속되지 않는다.

   4) 디바이스마다 화면의 크기가 다른 것을 고려하여 상대 단위인 %를 사용한다. 

   - **F** - viewwidth, viewheight > vw, vh라는 단위를 사용한다.

   5) id 값은 유일해야 하므로 중복되어서는 안된다.

   - **T** 



### 5. CSS 우선순위

- CSS는 우선 적용되는 순서가 존재 한다. 우선순위가 높은 순으로 나열 하시오.

```plainText
1. !important > CSS 종속성을 깨뜨리게 되고, 그렇게 되었을때 예상치 못한 결과가 발생할 수 있다. 기존까지 작업한 모든 레이아웃이 망가질 수도 있으므로, 특수한 상황이 아니라면 사용을 금한다.

2. Inline Style > css에 작성한 것이 아닌, 특별히 해당 태그에 작성한 것이다.

3. id 선택자 > id는 그 태그가 가지는 고유값

4. class 선택자 > 다수가 동일한 속성을 가질 수 있는 class 선택자

5. 요소 선택자 > p, div, a, h1 등 ... 태그자체에 스타일을 부여하는 것

6. 소스 순서 
```



