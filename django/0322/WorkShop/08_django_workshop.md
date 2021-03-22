# 08_Workshop



### 1. /accounts/

- 유저 목록을 출력하는 페이지를 나타낸다.

```python
@require_safe
def read(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'accounts/read.html', context)
```

![image-20210322202811247](08_django_workshop.assets/image-20210322202811247.png)



### 2. /accounts/signup/

- 회원가입 작성을 위한 페이지를 나타낸다.
- 유저를 생성하는 기능을 수행한다.

```python
@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:read')
    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/create.html', context)
```

![image-20210322202840264](08_django_workshop.assets/image-20210322202840264.png)

![image-20210322202856207](08_django_workshop.assets/image-20210322202856207.png)