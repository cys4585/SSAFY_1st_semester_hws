# 07_HomeWork

### 1. static 파일 기본 설정

- 개발자가 작성한 CSS 파일이나 넣고자 하는 이미지 파일 등이 Django 프로젝트 폴더 내부 의 ‘/assets’에 있다. ‘이 폴더 안에 Static 파일이 있다.’라고 Django 프로젝트에게 알려 주기 위하여 settings.py에 작성해야 하는 설정을 작성하시오. 

  ```python
  # settings.py
  
  STATICFILES_DIRS = [
      BASE_DIR / 'crud' / 'assets'
  ]
  ```

  

### 2. media 파일 기본 설정 

- 업로드 파일 저장 위치를 Django 프로젝트 폴더 내부의 ‘/uploaded_files’로 지정하고자 한 다. 이 때, settings.py에 작성해야 하는 설정을 모두 작성하시오. 

  ```python
  # settings.py
  
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / ProjectFolderName / 'uploaded_files'
  ```

  



### 3. Serving files uploaded by user during development 

- settings.py에 MEDIA_URL 값이 작성되어 프로젝트에 사용자가 업로드한 파일이 업로드 될 수 있게 되었다. 하지만 사용자가 실제 웹 페이지 내에서 이 파일을 조회 할 수 있도록 하기 위해선 업로드 된 파일에 대한 URL을 생성 해주는 설정이 필요하다. 빈칸 __(a)__, __(b)__, __(c)__, __(d)__에 들어 갈 코드를 작성하시오.

  ```python
  # project/urls.py
  
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatters = [
      ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```
  
  