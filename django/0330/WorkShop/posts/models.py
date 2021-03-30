from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    issue_a = models.CharField(max_length=50)
    issue_b = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Pick(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=10)
    count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.content


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pick = models.ForeignKey(Pick, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
