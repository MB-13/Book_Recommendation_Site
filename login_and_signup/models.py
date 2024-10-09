from django.db import models

# Create your models here.

class userInfo(models.Model):
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length = 150)
    emailAddress = models.EmailField()
    password = models.CharField(max_length=30)
    

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}"
    
