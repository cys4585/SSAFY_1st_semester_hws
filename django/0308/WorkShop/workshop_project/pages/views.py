from django.shortcuts import render
import random

# Create your views here.
def lotto(request):
    num_arr = [i for i in range(1, 46)]
    lotto_nums = random.sample(num_arr, 6)
    context = {
        'lotto_nums': lotto_nums,
    }
    return render(request, 'lotto.html', context)