from django import forms
from .models import Post, Comment, Pick


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('pick',)


class PickForm(forms.ModelForm):

    class Meta:
        model = Pick
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('post',)

    def __init__(self, post, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pick'].queryset = Pick.objects.filter(post=post)