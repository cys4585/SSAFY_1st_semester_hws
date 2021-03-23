# 09_Workshop

```python
@require_http_methods(['POST', 'GET'])
def change_password(request):
    if request.user.is_authenticated:
        pass
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)
```

