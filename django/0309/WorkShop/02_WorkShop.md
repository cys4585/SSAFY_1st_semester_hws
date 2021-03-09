### 02_WorkShop



![image-20210309152303277](02_WorkShop.assets/image-20210309152303277.png)



1. intro/urls.py

   ```python
   from django.contrib import admin
   from django.urls import path
   from pages import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('dinner/<str:menu>/<int:num>/', views.dinner),
   ]
   ```

2. pages.views.py

   ```python
   from django.shortcuts import render
   
   # Create your views here.
   def dinner(request, menu, num):
       context = {
           'menu': menu,
           'num': num,
       }
       return render(request, 'dinner.html', context)
   ```

3. templates/dinner.html

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
     <h1>저녁 메뉴</h1>
     <h1>저녁 먹을 사람?! {{num}}명</h1>
     <h1>어떤 메뉴?! {{menu}}</h1>
   </body>
   </html>
   ```
   
   