# 06_WorkShop

### 1.ImageField의 Optional Argument

- 사용자가 업로드한 파일들을 업로드 된 날짜에 따라 분류하고자 한다. 제시된 이미지와 같 이 저장 될 수 있도록 아래 링크를 참고하여 Media 파일 저장 경로를 설정하는 코드를 작성하시오.

  https://docs.python.org/3/library/time.html#time.strftime

  https://docs.djangoproject.com/en/3.1/ref/models/fields/#filefield

  ![image-20210318125709008](06_WorkShop.assets/image-20210318125709008.png)



```python
# settings.py

MEDIA_ROOT = BASE_DIR / 'media'
```

```python
# models.py

...
	image = models.ImageField(
    	upload_to='%Y/%m/%d/'
    )
```

