from operator import mod
from django.db import models

# Create your models here.
class poem(models.Model):
    title=models.CharField(max_length=20,null=False)
    author=models.CharField(max_length=10,null=False)
    paragraphs=models.TextField(max_length=100,null=False)

# class Author(models.Model):
#    author=models.CharField(max_length=10,null=False)

#class Title(models.Model):
#    title=models.CharField(max_length=20,null=False)

#class Paragraphs(models.Model):
#    paragraphs=models.TextField(max_length=100,null=False)