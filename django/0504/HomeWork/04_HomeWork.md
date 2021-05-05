# 04_HomeWork

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오. 

- Event Loop는 Call Stack이 비워지면 Task Queue의 함수들을 Call Stack으로 할당하 는 역할을 한다. 
  - `True`
- XMLHttpRequest(XHR)은 AJAX 요청을 생성하는 JavaScript API이다. XHR의 메서드 로 브라우저와 서버간의 네트워크 요청을 전송할 수 있다. 
  - `True`
- axios는 XHR(XMLHttpRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다. 
  - `True`



### 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

```javascript
console.log('Hello SSAFY!')

setTimeout(function () {
    console.log('I am from setTimeout')
}, 1000)

console.log('Bye SSAFY!')
```

	1. `console.log('Hello SSAFY!')`가 Call Stack으로 간다. 
 	2. `console.log('Hello SSAFY!')`가 실행되고 Call Stack에서 삭제된다
 	3. `setTimeout(function () {
         console.log('I am from setTimeout')
     }, 1000)`가 Call Stack으로 간다.
 	4. `function () {
         console.log('I am from setTimeout')
     }`가 Web API로 가고, Call Stack에서 삭제된다. 1000ms 동안 머무른다.
 	5. `console.log('Bye SSAFY!')`가 Call Stack으로 간다.
 	6. `console.log('Bye SSAFY!')`가 실행되고 Call Stack에서 삭제된다.
 	7. 1000ms 후에 
     `function () {
         console.log('I am from setTimeout')
     }`이 Task Queue로 이동한다.
 	8. Event Loop가 Call Stack이 비어있는 것을 확인하면 
     `function () {
         console.log('I am from setTimeout')
     }`을 Call Stack으로 보낸다.
 	9. `function () {
         console.log('I am from setTimeout')
     }`이 실행되고 Call Stack에서 삭제된다.



### 3. JS는 Event loop를 기반으로 하는 Concurrency model을 가지고 있다고 한다. Concurrency 키워드의 특징을 작성하고, 이와 비슷한 키워드로 비교되는 Parallelism의 개념과 두 개념의 차이점을 서술 하시오.

- Call Stack 
  - 요청이 들어올 때마다 해당 요청을 순차적으로 처리하는 Stack 형태의 자료구조
- Web API
  - JavaScript 엔진이 아닌 브라우저 영역에서 제공하는 API
  - setTimeout(), DOM event, AJAX로 데이터를 가져오는 시간이 소요되는 일들을 처리
- Task Queue
  - 콜백 함수가 대기하는 Queue 형태의 자료구조
  - main thread가 끝난 후 실행되어 후속 JavaScript 코드가 차단되는 것을 방지
- Event Loop
  - Call Stack이 비어있는지 여부 확인
  - 비어있는 경우 Task Queue에서 실행 대기중인 콜백이 있는지 확인
  - Task Queue에 대기중인 콜백이 있다면 가장 앞에 있는 콜백을 Call Stack으로 push

- 차이 
  - Concurrency : 동시에 실행되는 것 처럼 보이는 것
  - Parallelism : 실제로 동시에 작업이 처리가 되는 것