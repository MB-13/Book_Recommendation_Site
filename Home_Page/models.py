from django.db import models

# Create your models here.
class Book_Detail(models.Model):
    Title = models.CharField(max_length=400)
    Author = models.CharField(max_length=200,null=True)
    Genre = models.CharField(max_length=50,null=True)
    Description = models.CharField(max_length=8000,null=True)
    Publish_year = models.CharField(max_length=20,null=True)
    Cover_url = models.CharField(max_length=300,null=True)
    
    def __str__(self):
        return f"{self.Title}"
