from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    Author = models.ForeignKey(User , on_delete=models.CASCADE)
    Title = models.CharField(max_length=40)
    Text = models.TextField()
    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Author) + "\n" + self.Title
    

