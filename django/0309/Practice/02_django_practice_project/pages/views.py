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