# 05_Homework



## Problem

아래 작성된 views.py 의 코드 일부를 보고 문제에 알맞은 답을 서술 하시오.

```python
from django.shortcuts import render, redirect
from .froms import ArticleForm


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
	else:
        form = ArticleForm()
	context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

1. 왜 변수 context는 if else 구문과 동일한 레벨에 작성되어 있는가?
   - method가 POST 방식으로 요청이 왔다고 하더라도, if form.is_valid()에서 유효성 검사를 통과하지 못해 밖으로 빠져나오는 경우가 있을 수 있다. 그 때 return을 하기 위해서는 context가 필요하다.
2. 왜 request의 http method는 POST 먼저 확인하도록 작성하는가?
   - POST 요청에 대한 작업이 더 중요하고 복잡하기 때문에..?