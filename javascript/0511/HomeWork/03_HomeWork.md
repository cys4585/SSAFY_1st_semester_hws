# 03_HomeWork

### 1.아래의 설명을 읽고 T/F 여부를 작성하시오. 

- Vue는 컴포넌트 간 양방향 데이터 흐름을 지향하기 때문에 부모, 자식 컴포넌트 간의 데이터 전달 및 수정이 자유롭다. 

  - `False`

  - > Vue는 기본적으로 컴포넌트간 단방향 데이터 흐름을 지향한다. 그렇기 때문에 자식 컴포넌트 간 데이터 전달을 위해서는 부모 컴포넌트를 거쳐야만 한다.

- v-on 디렉티브는 해당 요소 또는 컴포넌트에서 특정 이벤트 발생 시 전달받은 함수 를 실행한다. 

  - `True`

  - ```vue
    <p v-on:event-name="functionName"></p>
    ```

- 컴포넌트에서 클릭 이벤트 발생 시 특정 함수를 실행하고자 할 때, @click 혹은 v-on:click 디렉티브를 사용한다. 

  - `False`

  - ```vue
    <Component @click.native="functionName"/>
    ```

- 부모 컴포넌트는 props를 통해 자식 컴포넌트에게 이벤트를 보내고 자식 컴포넌트 는 emit을 통해 부모 컴포넌트에게 데이터를 전달한다.

  - `False`

  - > 부모 컴포넌트는 props를 통해 자식 컴포넌트에게 데이터를 전달한다.
    >
    > 자식 컴포넌트는 emit을 통해 부모 컴포넌트에게 이벤트를 보낸다.



### 2. Vue는 단방향 데이터 흐름을 지향하는 프론트엔드 프레임워크다. 공식문서를 참고하여 그 이유를 서술하시오. 

​	 - 하위 컴포넌트가 실수로 부모의 상태를 변경하여 앱의 데이터 흐름을 추론하기 어렵게 만드는 것을 방지하기 위해

[링크](https://kr.vuejs.org/v2/guide/components.html#%EB%8B%A8%EB%B0%A9%ED%96%A5-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%9D%90%EB%A6%84)



### 3. 다음은 자식 컴포넌트에서 이벤트를 발생시켜 부모 컴퍼넌트의 함수를 실행하는 코드 이다, 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오. 

- Input 컴포넌트의 버튼을 누르면 addTodo 이벤트가 발생한다. (이벤트 발생 시 data의 text 값도 함께 전달한다.) 
- TodoList 컴포넌트에서 addTodo 이벤트가 발생하면, onAddTodo 함수를 실행한 다. 
- onAddTodo 함수에서는 자식 컴포넌트에서 전달받은 값을 console.log 함수를 통해 출력한다.

```vue
<!-- Input.vue -->
<template>
  <div>
	<input v-model="text" type="text">
    <button @click="onClick">추가</button>
  </div>
</template>

<script>
  export default {
    name: 'Input',
	data: function () {
      return {
        text: '',
	  }
	},
    methods: {
      onClick: function () {
        __(a)__('addTodo', this.text)
      }
    }
  }
</script>
```

```vue
<!-- TodoList.vue -->
<template>
  <Input __(b)__ />
</template>

<script>
  import Input from './Input';
    
  export default {
    name: 'TodoList',
	components: {
      Input: Input
    }
    methods: {
	  __(c)__
    }
  }
</script>
```

- `__(a)__` : `this.$emit`
- `__(b)__` : `@addTodo="onAddTodo"`
- `__(c)__` : `onAddTodo: function (inputText) {console.log(inputText)}`











