from django.db import models
from Home_Page.models import Book_Detail_2
# Create your models here.

class SearchEmbedModel(models.Model):

    Book = models.OneToOneField(Book_Detail_2,on_delete=models.CASCADE,related_name="title_embed")
    TitleEmbed = models.JSONField(null=True)

    def __str__(self):
        return f"{self.Book.Title}"