# 02_HomeWork

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오. 

- let & const 키워드로 선언한 변수와 var 키워드로 선언한 변수의 유일한 차이점은 변수의 유효범위이다.
  - `False`
  - 재선언이 가능하다 : var
  - 재선언이 불가능하다 : let, const
  - 재할당이 가능하다 : var, let
  - 재할당이 불가능하다 : const

- “값이 없음”을 표현하는 값으로 null과 undefined 두 종류가 있으며, 둘 다 typeof 연산자에서 undefined가 반환된다.
  - `False`
  - typeof(null) : object
    - 실제로는  object이 아닌 원시 타입(Number, String, Boolean같은 Primitive type 중 하나)이다.
  - typeof(undefined) : undefined
- for in 문을 통해 배열의 각 요소를 순회할 수 있다. 
  - `True`
  - 순회가 가능은 하지만, for in 문은 순서를 보장하지 않기 때문에, 권장되는 방법은 아니다. (for of 문을 통해 순서대로 순회할 수 있다.)
- ‘==’ 연산자는 두 변수의 값과 타입이 같은지 비교하고 같다면 true 아니면 false 를 반환한다. 
  - `False`
  - 암묵적 타입 변환을 통해 타입을 일치시킨 후, 두 변수의 값이 같으면 true를 아니면 false를 반환한다.
- JavaScript에서 함수는 변수에 할당, 인자로 전달할 수 있으나 함수의 결과값으로 반환할 수는 없다. 

  - `False`
  - 함수의 결과값을 변수에 반환할 수 있다.



### 2. 다음의 Array Helper Method의 동작을 간략히 서술하시오.

- map, filter, find, every, some, reduce
- 예) forEach - 배열의 요소를 하나씩 순회한다. 
  - array.map(callback(...)) : array의 모든 요소를 하나씩 callback 함수의 인자로 넣고, callback 함수의 반환 값을 요소로 하는 새로운 배열을 반환한다.
  - array.filter(callback(...)) : array의 모든 요소를 하나씩 callback 함수의 인자로 넣고, callback 함수의 반환값이 참인 요소들만 모아서 새로운 배열을 반환한다.
  - array.find(callback(...)) : array의 모든 요소를 하나씩 callback 함수의 인자로 넣고, callback 함수의 반환값이 참이면 해당 요소를 반환(for 반복문의 break 느낌...)한다. 만약 반환값이 참인 요소가 없으면 undefined를 반환한다.
  - array.every(callback(...)) : array의 모든 요소를 하나씩 callback 함수의 인자로 넣고, 모든 요소에 대해 callback 함수의 반환값이 참이면 true를, 하나라도 반환값이 거짓인 요소가 있으면 false를 반환한다.
  - array.some(callback(...)) : array의 모든 요소를 하나씩 callback 함수의 인자로 넣고, callback 함수의 반환값이 참인 경우가 한 번이라도 있으면 true를, 모든 요소에 대해 반환값이 거짓인 경우 false를 반환한다.
  - array.reduce(callback(acc, element[, index[, array]])[, initialValue]) : 
    - array의 모든 요소를 하나씩 callback 함수의 인자(element)로 넣고, callback 함수의 반환값들을 acc에 누적 후 반환한다. initialValue는 optional한 매개변수로, 최초 callback함수 호출 시 acc에 할당되는 값이다. (initialValue에 값을 할당하지 않으면 array의 첫번째 값이 사용된다.)



### 3. 아래의 숫자 배열에 map 함수를 사용하여, 모든 아이템에 3제곱을 한 새로운 배열을 만드는 코드를 작성하시오.

```javascript
const nums = [1, 2, 3, 4]

const newNums = nums.map(num => num * num * num)
console.log(newNums)
```
