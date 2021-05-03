# 03_HomeWork

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오. 

- JavaScript는 single threaded 언어로 한번에 한가지 일 밖에 처리하지 못한다. 

  - `True`

- setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이 완료 되면 Call Stack에 바로 할당된다. 

  - `False`
  - Web API에서 작업이 완료되면 Task Queue로 이동하게 되고, 
    Event Loop가 Call Stack이 비어있는지 확인 후, 비어있다면, Task Queue에 쌓여있는 완료된 처리들을 Call Stack으로 옮긴다.

- Prmoise 객체를 생성할 때 인자로 받는 callback 함수인 resolve와 reject는 비동기 처 리가 성공/실패 했을 경우 어떠한 값을 전달할지 결정한다. 

  - `True`

- Promise 객체의 .then 메서드는 오류 없이 resolve 되었을 때 실행되는 함수이며, .catch 메서드는 도중에 오류가 발생하여 reject 되었을 때 실행되는 함수이다. 

  - `True`

  

### 2. JavaScript에서 동기와 비동기 함수의 차이점을 서술하시오.

- 동기 (Synchronous)
  - 순차적, 직렬적으로 task를 수행한다.
  - 요청을 보낸 후 응답을 받아야만 다음 동작이 이루어진다. (blocking)
- 비동기 (Asynchronous)
  - 병렬적으로 task를 수행한다.
  - 요청을 보낸 후 응답을 기다리지 않고, 다음 동작이 바로 이루어진다. (non-blocking)
    즉, 요청을 보내놓고 다음 task를 진행한다.



### 3. 다음은 axios를 사용하여 API 서버로 요청을 보내고, 응답 데이터를 출력하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

```javascript
axios.__(a)__('https://api.example.xom/data')
	.__(b)__(function (response) {
    	console.log(__(c)__)
	})
```

- `__(a)__` : get
- `__(b)__` : then
- `__(c)__` : response