from django.db import models

# Create your models here.
class poem(models.Model):
    title=models.CharField(max_length=20,null=False)
    author=models.CharField(max_length=10,null=False)
    paragraths=models.TextField(max_length=100,null=False)