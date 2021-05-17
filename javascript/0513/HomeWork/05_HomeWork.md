# 04_HomeWork

### 1.다음은 Vuex로 구성된 하나의 숫자를 counting하는 store이다. (a), (b), (c)에 들어갈 코드를 작성하시오. 

- increment mutation이 호출되면 state.count를 1만큼 증가시킨다.

```javascript
const store = new __(a)__ ({
    state: {
        count: 0,
    },
    mutations: {
        increment: function (state) {
            __(b)__
        }
    },
    actions: {
        increment: function (context) {
            __(c)__
        }
    }
})
```

- `__(a)__` : Vuex.Store
- `__(b)__` : state.count += 1
- `__(c)__` : context.commit('increment')

