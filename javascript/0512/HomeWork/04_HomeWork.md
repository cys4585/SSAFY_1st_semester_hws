# 04_HomeWork

### 1.아래의 설명을 읽고 T/F 여부를 작성하시오. 

- Vue 프로젝트에서 상태 관리를 하기 위해서는 반드시 Vuex를 설치해야 한다. 
  - `True`
- mutation은 반드시 state를 수정하기 위해서만 사용되어야 한다. 
  - `True`
- mutation은 store.dispatch로, action은 store.commit으로 호출할 수 있다. 
  - `False`
  - store.dispatch -> action
  - store.commit -> mutation
- state는 data와 동일하고, getters는 computed와 동일한 동작을 한다. 
  - `True`



### 2. Vuex에서 action과 mutation의 역할과, 두 함수의 차이를 서술하시오.

- action 
  - 비동기적 작업
  - mutation를 통해 state를 변경
  - 데이터 fetch 및 처리
- mutation
  - 동기적 작업
  - state를 직접적으로 변경