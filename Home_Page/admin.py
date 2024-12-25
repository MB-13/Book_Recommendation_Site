from django.contrib import admin

from .models import Book_Detail,Book_Detail_2,BestSeller,BookembedModel
# Register your models here.

admin.site.register(Book_Detail)
admin.site.register(Book_Detail_2)
admin.site.register(BestSeller)
admin.site.register(BookembedModel)