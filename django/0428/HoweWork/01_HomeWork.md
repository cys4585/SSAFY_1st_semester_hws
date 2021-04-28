# 01_HomeWork

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오. 

- document.createElement 메서드를 통해 HTML 요소를 생성할 수 있다. 

  - `True`

- EventTarget.addEventListener(type, listener)에서 listener에 작성되는 콜백 함수의 첫번째 매개변수는 발생한 이벤트를 설명하는 Event에 기반한 객체이다.

  - ```javascript
    const button = document.querySelector('.btn')
    
    button.addEventListener('click', function (event) {
        
    })
    ```

  - `True`

- event.preventDefault 메서드를 통해 이벤트 동작을 취소할 수 있다. 

  - ```javascript
    const button = document.querySelector('.btn')
    
    button.addEventListener('submit', function (event) {
        event.preventDefault()
    })
    ```

  - `True`

- 부모 노드에서 자식 노드를 추가하는 유일한 방법은 append 메서드 뿐이다. 

  - `False`
  - appendChild 메서드
  - append() : 여러 자식 노드 추가
  - appendChild() : 하나의 자식 노드만 추가



### 2. DOM Event에는 다양한 종류의 Event가 존재한다. 아래 제시된 Event들이 각각 어떤 시점에 발생하는지 다음 MDN 문서를 참고하여 간단하게 작성하시오. 

[MDN](https://developer.mozilla.org/ko/docs/Web/Events)

```
click - 클릭
mouseover - 마우스 올라갔을 때
mouseout - 마우스 벗어났을 때
keydown - 키 눌렸을 때
keyup - 키 뗐을 때
load - 로드 됐을 때
scroll - 스크롤 썼을 때
change - 상태 또는 요소의 내용이 변경될 때
input - 요소의 텍스트 내용이 사용자를 통해 변경될 때
```





### 3. 다음은 버튼을 클릭했을 때, 콘솔창을 통해 메시지를 확인하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

```javascript
const button = document.__(a)__('button')

button.__(b)__(__(c)__, function () {
    console.log('Button Clicked!')
})
```

- `__(a)__` : querySelector
- `__(b)__` : addEventListener
- `__(c)__` : 'click'