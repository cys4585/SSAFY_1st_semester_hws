# 01_HomeWork

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오. 

- SPA는 Single Pattern Application의 약자이다. 
  - `False`
  - Single Page Application
- SPA는 웹 애플리케이션에 필요한 모든 정적 리소스를 한 번에 받고, 이후부터는 페이 지 갱신에 필요한 데이터만 전달받는다. 
  - `True`
- Vue.js에서 말하는 ‘반응형’은 데이터가 변경되면 이에 반응하여, 연결된 DOM이 업데이트되는 것을 의미한다. 
  - `True`



### 2. MVVM은 무엇의 약자이고, 해당 패턴에서 각 파트의 역할은 무엇인지 간단히 서술하시 오. 

- Model, View, View Model 
- MVVM Pattern : 애플리케이션 로직을 UI로부터 분리하기 위해 설계된 디자인 패턴
- Model 
  - javascript objects
  - Vue Instance 내부에서 data로 사용되는데 이 값이 바뀌면 View(DOM)가 반응
- View
  - DOM(HTML)
  - Data의 변화에 따라서 바뀌는 대상
- ViewModel
  - Vue Instance
  - View와 Model 사이에서 Data와 DOM에 관련된 모든 일을 처리
  - ViewModel을 활용해 Data를 얼마만큼 잘 처리해서 보여줄 것인지(DOM)를 고민하는 것



### 3. 다음의 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.

```html
<div id="app">
    {{ __(a)__ }}
</div>

<script>
  const app = __(B)__({
    el: __(c)__,
    data: {
  	  message: 'Hello World!'      
    }
  })
</script>
```

- `__(a)__` : message
- `__(b)__` : new Vue
- `__(c)__` : '#app'



### 4. 아래의 설명을 읽고 T/F 여부를 작성하시오. 

- 동일한 요소에 v-for와 v-if 두 디렉티브가 함께 작성된 경우, 매 반복 시에 v-if의 조건문으로 요소의 렌더링 여부를 결정한다. 

  - `True`

- v-bind 디렉티브는 “@“, v-on 디렉티브는 “:” shortcut(약어)을 제공한다. 

  - `False`
  - `@` : v-on
  - `:` : v-bind 

- v-model 디렉티브는 input, textarea, select 같은 HTML 요소와 단방향 데이터 바인딩을 이루기 때문에 v-model 속성값의 제어를 통해 값을 바꿀 수 있다.

  - `False`
  - 양방향 데이터 바인딩
  - 단방향 데이터 바인딩 -> v-bind
  
  

### 5. computed와 watch의 개념과 그 차이에 대해서 간단히 서술하시오. 

- computed 
  - 데이터를 기반으로 하는 계산된 속성
  -  함수의 형태로 정의하지만 함수가 아닌 함수의 반환값이 바인딩 됨
  - 종속된 대상을 따라 저장(캐싱) 됨
  - 종속된 대상이 변경될 때만 함수를 실행
  - 즉, Date.now() 처럼 아무 곳에도 의존하지 않는 computed 속성의 경우 절대로 업데이트되지 않음
  - 반드시 반환값이 있어야 함
- watch
  - 데이터를 감시
  - 데이터에 변화가 일어났을 때 실행되는 함수
- 차이
  - computed는 선언형 프로그래밍 방식 (계산해야 하는 목표 데이터를 정의하는 방식)
    watch는 명령형 프로그래밍 방식 (감시할 데이터를 지정하고 그 데이터가 바뀌면 어떤 함수를 실행하라는 방식)
  - computed는 특정 데이터를 직접적으로 사용/가공하여 다른 값으로 만들 때 사용
    watch는 특정 데이터의 변화 상황에 맞춰 다른 data 등이 바뀌어야할 때 주로 사용



### 6. 다음은 홀수 데이터만 렌더링하는 Vue Application의 예시이다. 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.

```html
<div id="app">
    <div __(a)__="(num, __(b)__) in __(c)__" :key="__(b)__">
      <p>{{ num }}</p>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        nums: [1, 2, 3, 4, 5]
      },
      computed: {
        oddNumbers: function () {
          return this.nums.filter((num) => {
            return num % 2 == 1
          })
        }
      }
    })
  </script>
```

- `__(a)__` : v-for
- `__(b)__` : idx
- `__(c)__` : oddNumbers

