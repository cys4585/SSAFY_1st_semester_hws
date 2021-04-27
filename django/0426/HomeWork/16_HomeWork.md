# 16_HomeWork



### 1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오. 

- URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다. 

  - **True**
- HTTP Method는 GET과 POST 두 종류가 있다. - 일반적으로 URI 마지막에 슬래시( / )는 포함하지 않는다. 

  - **False**
  - HEAD, PUT, DELETE, CONNET, OPTIONS, TRACE, PATCH 도 있다.
  - [HTTP Method](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods)
- 일반적으로 URI  마지막에 슬래시( / )는 포함하지 않는다. (trailing slash)
  - **True**
- `https://www.fifa.com/worldcup/teams/team/43822/create/`는 계층 관계를 잘 표현 한 RESTful한 URI라고 할 수 있다.
  - **False**
    1. 자원에 대한 행위는 HTTP Method로 표현해야 한다. (create는 POST)
       - POST `https://www.fifa.com/worldcup/teams/team/43822/`
    2. 계층 관계가 명확하지 않다.
       - `https://www.fifa.com/worldcup/teams/43822/`



### 2. 다음의 HTTP status code의 의미를 간략하게 작성하시오. 

- 200
  - 요청이 성공적으로 처리됨
- 400 
  - 유효하지 않은 요청 (서버가 요청을 이해할 수 없음)
- 401 
  - 유효한 인증 자격 증명이 없기 때문에 요청이 적용되지 않음
- 403 
  - 권한 없음
  - 클라이언트 오류 상태 응답 코드는 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미
- 404 
  - 서버가 요청받은 리소스를 찾을 수 없다는 것을 의미
- 500
  - 서버 에러 응답 코드는 요청을 처리하는 과정에서 서버가 예상하지 못한 상황에 놓였다는 것을 나타냄



### 3. 아래의 모델을 바탕으로 Serializer를 정의하려 한다. serializers.py 파일에 StudentSerializer를 작성하시오.

```python
class Student(models.Model):
    name = models.TextField()
    age = models.CharField(max_length=20)
    address = models.TextField()
```

```python
# serializers.py
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
```



### 4. Serializers의 의미를 DRF(Django REST Framework) 공식 문서를 참고하여 간단하게 설명하시오.