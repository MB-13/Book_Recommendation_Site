from django.shortcuts import render
from django.views import View
from Home_Page.models import Book_Detail
# Create your views here.

class GenreView(View):
    def get(self,request,genre):
        
        genre_book_list = Book_Detail.objects.filter(Genre=genre.lower())
        return render(request,"Genre_Page/genre.html",{"genre":genre,"genre_book":genre_book_list})
