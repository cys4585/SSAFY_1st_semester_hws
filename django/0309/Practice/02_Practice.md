# 02_Practice



![image-20210309164127765](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210309164127765.png)

1. pages/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('lotto/', views.lotto),
]

```



1. pages/views.py

```python
from django.shortcuts import render
import random
import requests

# Create your views here.
def lotto(request):
    lotto_url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'
    lotto_response = requests.get(lotto_url)
    lotto_data = lotto_response.json()

    lotto_nums = []
    lotto_nums.append(lotto_data['drwtNo1'])
    lotto_nums.append(lotto_data['drwtNo2'])
    lotto_nums.append(lotto_data['drwtNo3'])
    lotto_nums.append(lotto_data['drwtNo4'])
    lotto_nums.append(lotto_data['drwtNo5'])
    lotto_nums.append(lotto_data['drwtNo6'])
    bonus_num = lotto_data['bnusNo']

    numbers = range(1, 46)
    # 1등 6개 / 2등 5개 + 보너스 / 3등 5 / 4등 4개 / 5등 3개 / 꽝 : 0~2개
    ranks_count = [0] * 6
    for _ in range(1000):
        cnt = 0
        buy_lotto = random.sample(numbers, 7)
        buy_bonus = buy_lotto.pop()
        buy_lotto.sort()
        # print(buy_lotto, '+', buy_bonus)
        for j in range(6):
            if lotto_nums[j] == buy_lotto[j]: cnt += 1
        if cnt == 6: ranks_count[0] += 1
        elif cnt == 5:
            if bonus_num == buy_bonus: ranks_count[1] += 1
            else: ranks_count[2] += 1
        elif cnt == 4: ranks_count[3] += 1
        elif cnt == 3: ranks_count[4] += 1
        else: ranks_count[5] += 1
    context = {
        'lotto_nums': lotto_nums,
        'bonus_num': bonus_num,
        'ranks_count': ranks_count,
    }
    return render(request, 'pages/lotto.html', context)
```



1. templates/pages/lotto.html

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
  <h1>로또 당첨 횟수를 알아보자.</h1>
  <hr>
  <h3>이번 회차 당첨 번호: {{lotto_nums}} + {{bonus_num}}</h3>
  <ul>
    {% for count in ranks_count %}
      <li>{{ forloop.counter }}등 : {{count}}번</li>
    {% endfor %}
  </ul>
</body>
</html>
```

