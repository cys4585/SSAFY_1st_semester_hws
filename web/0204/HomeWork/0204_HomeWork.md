# 0204_HomeWork

### 1. CSS flex-direction

- Flex box의 주축을 변경하는 flex-direction의 4가지 값과 각각의 특징을 작성하시오.
  - row : 주축을 가로로 설정 (default)
  - column : 주축을 세로로 설정
  - row-reverse : 주축을 가로로 설정, 순서를 오른쪽에서 왼쪽으로 설정
  - column-reverse : 주축을 세로로 설정, 순서를 아래쪽에서 위쪽으로 설정



### 2. Bootstrap flex-direction

- flex-direction의 4가지 요소와 대응하는 bootstrap 클래스를 작성하시오.
  - flex-row
  - flex-column
  - flex-row-reverse
  - flex-column-reverse



### 3. align-items

- align-items 속성의 4가지 값과 각각의 특징을 작성하시오.
  - flex-start : 교차축 방향의 시작선에 정렬
  - flex-end : 교차축 방향의 끝선에 정렬
  - center : 교차축 방향의 중앙에 정렬
  - stretch : flex 컨테이너 최대 길이로 늘리기
  - baseline : text의 baseline을 기준으로 정렬



### 4. flex-flow

- flex-flow 속성은 두가지 속성의 축약형이다. 올바르게 짝지어진 것을 고르시오.

  **(1) flex-direction, flex-wrap**
  (2) flex-direction, align-items
  (3) justify-content, flex-wrap
  (4) justify-content, align-items



### 5. Bootstrap Grid System

- 하단 코드에 Bootstrap Grid System을 적용시키고자 할 때, __(a)__, __(b)__ 각각에 입력해야 할 클래스 이름을 작성하시오.

```html
<div class="(a)">
    <div class="(b)">
        <div class="col-(c)-(d)"></div>
    </div>
</div>
```

	- a : container	
	- b : row



### 6. Breakpoint prefix

- Bootstrap Grid System에서 요소의 크기를 지정하기 위해서는 상단 코드와 같은 형태로 클래스 이름을 지정해야 한다.

  1. __(c)__에 들어갈 수 있는 값과 그 값들이 가지는 의미를 작성하시오.

     - 디바이스나 화면 크기에 따라서 반응하는 웹을 구현할 수 있도록 한다.
       - sm : small
       - md : medium
       - lg : large
       - xl : extra large
       - xxl : extra extra large

  2. __(d)__에 들어갈 수 있는 값과 그 값들이 가지는 의미를 작성하시오.

     - `12이하의 정수`

     - 12개로 나눈 공간에서 몇 칸을 차지하는지 표시한다.

       [bootstrap breakpoint](https://getbootstrap.com/docs/5.0/layout/breakpoints/)