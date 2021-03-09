# 01_WorkShop



### 1. Django Project

1. intro/urls.py

   ```django
   from django.contrib import admin
   from django.urls import path
   from pages import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('lotto/', views.lotto),
   ]
   ```

2. pages/views.py

   ```django
   from django.shortcuts import render
   import random
   
   # Create your views here.
   def lotto(request):
       num_arr = range(1, 46)
       lotto_nums = random.sample(num_arr, 6)
       context = {
           'lotto_nums': lotto_nums,
       }
       return render(request, 'lotto.html', context)
   ```

3. templates/lotto.html

```django
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>제 OOO회 로또 번호 추천</h1>
  <p>SSAFY님께서 선택하신 로또 번호는 {{lotto_nums}}입니다.</p>
</body>
</html>
```

