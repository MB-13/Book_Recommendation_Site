from django.db import models
from Home_Page.models import Book_Detail_2
import uuid

# Create your models here.

class userInfo(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length = 150)
    emailAddress = models.EmailField()
    password = models.CharField(max_length=30)
    readLater = models.ManyToManyField(Book_Detail_2,related_name="user_readLater")
    

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}"
    
