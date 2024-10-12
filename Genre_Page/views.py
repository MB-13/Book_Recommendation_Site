from django.shortcuts import render
from django.views import View
# Create your views here.

class GenreView(View):
    def get(self,request,genre):
        print(genre)
        return render(request,"Genre_Page/genre.html")
