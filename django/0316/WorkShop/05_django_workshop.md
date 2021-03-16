# 05_Workshop



## Django Model Form

아래의 코드들을 참고하여 각 문항에 답하시오.

```python
# models.py
class Reservation(models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField()
```

​	1) 모델 폼을 정의하기 위해 빈칸에 들어갈 코드를 작성하시오.

```python
# forms.py
from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        field = '__all__'    
```

​	2) 글 작성 기능을 구현하기 위해 다음과 같이 코드를 작성하였다. 서버를 실행시킨 후 기능을 테스트 해보니 특정 상황에서 문제가 발생하였다. 이유와 해결방법을 작성하시오.

```python
# views.py
def create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk)
	else:
        form = ReservationForm()
        context = {
            'form' : form
        }
        return render(request, 'reservations/create.html', context)
```

	- 이유 : POST 방식의 요청이 왔을 때, 유효성 검사를 통과하지 못하면, 응답을 위한 return을 하지 않는다.
	- 해결방법 : else 문의 context와 return문을 밖으로 뺀다. -> POST 요청에서 유효성 검사를 통과하지 못하는 경우 ModelForm과 함께 create.html을 보여준다.



​	3) 글 수정 기능을 구현하기 위해 빈칸에 들어갈 코드를 작성하시오.

```python
# views.py
def update(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    if request.method = 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
			reservation = form.save()
            return redirect('reservations:detail', reservation.pk)
	else:
        form = ReservationForm(instance=reservation)
	context = {
        'reservation': reservation,
        'form': form
    }
    return render(request, 'reservations/update.html', context)
```



​	4) 글 수정 기능을 구현하기 위해 빈칸에 들어갈 수 있는 코드를 모두 작성하시오.

```django
<h2>edit</h2>
<form action="{% url 'reservations:update' reservation.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    {{ form.as_table }}
    {{ form.as_ul }}
    <input type="submit" value="submit">
</form>
```

