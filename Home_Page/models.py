from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

genre_choices = [
    ("biography","biography"),
    ("children","childrean"),
    ("fantasy","fantasy"),
    ("fiction","fiction"),
    ("mystery","mystery"),
    ("non-fiction","non-fiction"),
    ("romance","romance"),
    ("science","science"),
    ("science fiction","science fiction"),
]

# Create your models here.
class Book_Detail(models.Model):
    Title = models.CharField(max_length=400)
    Author = models.CharField(max_length=200,null=True)
    Genre = models.CharField(max_length=50,null=True,choices=genre_choices)
    Description = models.CharField(max_length=8000,null=True)
    Publish_year = models.CharField(max_length=20,null=True)
    Cover_url = models.CharField(max_length=300,null=True)
    Rating = models.FloatField(null=True,default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    Rating_Count = models.BigIntegerField(null=True,default=0,validators=[MinValueValidator(0)])
    weighted_avg = models.FloatField(null=True)
    
    
    nor_mean = 90523
    rate_mean = 3.25
    
    def __str__(self):
        return f"{self.Title}"
    
    def save(self,*args, **kwargs):
        self.weighted_avg = ((self.Rating * self.Rating_Count) + (self.nor_mean*self.rate_mean)) / (self.Rating_Count + self.nor_mean)
        super(Book_Detail,self).save(*args, **kwargs)
