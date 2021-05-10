# 02_HomeWork

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오. 

- Vue의 Life Cycle Hook에서 created Hook은 Vue template에 작성한 요소들이 DOM에 다 그려지는 시점에 실행된다. 

  - `False`

  - > DOM에 추가되기 전에 실행된다.
    >
    > 서버단 렌더링 모두에서 처리해야할 일이 있다면 Creaion 단계에서 하면된다. 아직 컴포넌트가 DOM에 추가되기 전이기 때문에 DOM에 접근하거나 this.$el를 사용할 수 없다.
    >
    > - Creation 단계(컴포넌트 초기화 단계)
    >   - beforeCreate Hook
    >     - data와 events가 세팅되기 전
    >   - created Hook
    >     - data와 events가 활성화되어 접근할 수 있다. 여전히 템플릿과 가상DOM은 마운트 및 렌더링되지 않은 시점이다.

- npm은 Node Package Manager의 약자이며, npm을 통해 설치한 package 목록은 package.json 파일에 자동으로 작성된다. 

  - `False`

  - > npm install <package_name> 만 하게되면, package.json에 포함되지 않는다.
    >
    > npm install <package_name> --save 명령어를 입력해 주어야 package.json의 dependency가 추가된다.

- Vue CLI를 통해 만든 프로젝트는 브라우저가 아닌 node.js 환경이기 때문에 DOM 조작이나 Web API 호출 등 Vanilla JS에서의 기능을 사용할 수 없다. 

  - `False`



### 2. Vue Router에서 설정하는 history mode가 무엇을 뜻하는지 서술하시오. 

- 페이지를 다시 로드하지 않고 URL을 탐색할 수 있는 모드



### 3. Vue Life Cycle Hook을 참고하여, 다음 Vue application을 실행했을 때 console 창에 출 력되는 메시지를 작성하시오.

```vue
<script>
	export default {
        name: 'HelloWorld',
        created: function () {
            console.log('created!')
        },
        mounted: function () {
            console.log('mounted!')
        },
        updated: function () {
            console.log('updated!')
        },
    }
</script>
```

```
created!
mounted!
```

