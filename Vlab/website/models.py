from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related

# Create your models here.
class Post(models.Model):

    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    formlink = models.URLField(max_length=500)

