from django.db import models

# Create your models here.
class Image(models.Model):
    photo=models.ImageField(upload_to="myimage")
    date=models.DateTimeField(auto_now_add=True)

    

from django.contrib.auth.models import User

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)