# 0201_WorkShop

### 1. img tag

아래 그림과 같은 폴더 구조가 있다. resume.html에서 코드를 작성 중일 때, image 폴더 안의 my_photo.png를 보여주는 ![img]() tag를 작성하시오. 단, 이미지가 제대로 출력되지 않을 때는 ssafy 문자열이 출력 되도록 작성하시오.



### 2. 파일 경로

위와 같이 경로를 __(a)__로 작성 할 시, github에 업로드 하거나 전체 폴더의 위치가 변경 되었을 때 이미지를 불러 올 수 없게 된다. 이를 해결 하려면 이미지 경로를 __(b)__ 로 바꾸어 작성하면 된다. __(a)__와 __(b)__에 들어갈 말과 __(b)__ 로 변경한 코드를 작성하시오.

- a : 절대 경로
- b : 상대 경로

```html
<!-- 절대 경로 -->
<img 
    src="C:\Users\USER\Desktop\hws\python\0201\WorkShop\image\ssafy.png"
    alt="SSAFY">

<!-- 상대 경로 -->
<!-- 현재 작업중인 파일의 상위 폴더로 가기 위해 .. 입력 -->
<!-- 상위폴더에 있는 image\ssafy.png -->
<img 
	src="..\image\ssafy.png"
    alt="SSAFY">
```



### 3. Hyper Link

출력된 my_photo.png 이미지를 클릭하면 ssafy.com으로 이동하도록 하시오.

```html
<!-- a 태그의 내부에 들어올 수 있는 요소는 모든 것들이 가능하다. 단순 텍스트 뿐만 아니라, 이미지 등도 가능하다. -->
  <a href="https://www.ssafy.com">
    <img src="..\image\ssafy.png" alt="SSAFY">  
  </a>
```



### 4. 선택자

1) 아래의 코드를 작성하고 결과를 확인 하시오.

```html
  <div id="ssafy">
    <h2>어떻게 선택 될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
  </div>
```

```css
    #ssafy > p:nth-child(2) {
      color: red;
    }
```

- 결과 : 첫번째 단락 p 태그의 text color가 red로 변경된다.

2) nth-child를 nth-of-type으로 변경하고 결과를 확인 하시오.

```css
    #ssafy > p:nth-of-type(2) {
      color: blue;
    }
```

- 두번째 단락 p 태그의 text color가 red로 변경된다.

3) 작성한 코드를 참고하여 nth-child()와 nth-of-type()의 차이점을 작성하시오.

- element:nth-child(n)
  - 부모의 자식들중에 n번째 요소를 선택
  - 부모의 모든 자식들 중, n번째
  - 단, 부모의 모든 자식들 중, n번째가 해당하는 태그가 아니면 선택되지 않는다.
- element:nth-of-type(n)
  - 부모의 자식들 중에 해당하는 element 중, n번째를 선택