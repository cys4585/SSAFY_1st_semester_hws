# 03_HomeWork

### 1. Model 반영하기

아래 그림과 같이 Django에서 선언한 Model을 실제 Database에 반영하는 과정을 뜻하는 용어와 이와 관련된 명령어들을 작성하시오

```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```

- Migrations
- 명령어
  - makemigrations
    - model을 변경한 것에 기반한 새로운 마이그레이션(like 설계도)을 만들 때 사용
  - migrate
    - 마이그레이션을 DB에 반영하기 위해 사용
    - 설계도를 실제 DB에 반영하는 과정
    - 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸
  - sqlmigrate
    - 마이그레이션에 대한 SQL 구문을 보기 위해 사용
    - 마이그레이션이 SQL 문으로 어떻게 해석되어서 동작할지 미리 확인할 수 있음
  - showmigrations
    - 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
    - migrate 됐는지 안됐는지 여부를 확인할 수 있음

### 2. Model 변경사항 저장하기

위에서 선언한 Model을 Database에 최종 반영하기 전에 Model의 변경 사항을 저장하고자 한다. 이를 위한 명령어를 수행했을 때 생성되는 파일의 내용을 확인하고, 해당 내용에 대응 되는 SQL문을 확인하여 작성하시오.

- BEGIN;

- CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL);
- COMMIT;

### 3. Python Shell

Django에서 사용 가능한 모듈 및 메서드를 대화식 Python Shell에서 사용하려고 할 때, 어떠한 명령어를 통해 해당 Shell을 실행할 수 있는지 작성하시오.

- pip install django-extensions
- settings.py
  - INSTALLED_APPS = [... , 'django_extensions', ...]

- python manage.py shell_plus

### 4. Django Model Field

Django에서 Model을 정의할 때 사용할 수 있는 필드 타입을 5가지 이상 작성하시오.

- CharField
- TextField
- DateTimeField
- AutoField
- FormField
- FloatField
- ImageField
- EmailField