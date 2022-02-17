from django.db import models

# Create your models here.
class Poem(models.Model):
    title=models.CharField(max_length=20,null=False)
    author=models.CharField(max_length=10,null=False)
    paragraphs=models.TextField(max_length=100,null=False)
    def __str__(self):
        return self.title

# class Author(models.Model):
#    author=models.CharField(max_length=10,null=False)

#class Title(models.Model):
#    title=models.CharField(max_length=20,null=False)

#class Paragraphs(models.Model):
#    paragraphs=models.TextField(max_length=100,null=False)