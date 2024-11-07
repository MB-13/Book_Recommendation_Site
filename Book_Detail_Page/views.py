from django.shortcuts import render
from django.views import View
from Home_Page.models import Book_Detail_2,BestSeller
# Create your views here.

class DetailView(View):
    def get(self,request,Id):
        book_obj = Book_Detail_2.objects.get(id=Id)
        # bestseller_obj = BestSeller.objects.all()
        book_details = {
            "title": book_obj.Title,
            "author": book_obj.Author,
            "genres": book_obj.Genre,
            "description": book_obj.Description,
            "image_url": book_obj.Cover_url,
            "pub_year": book_obj.Publish_year,
            "rating": book_obj.Rating,
            "rating_count": book_obj.Rating_Count,
            # "bestseller_obj": bestseller_obj,

        }
        return render(request,"Book_Detail_Page/book_detail.html",book_details)
    
class BestSelDetailView(View):
    def get(self,request,Id):
        book_obj = BestSeller.objects.get(id=Id)
        book_details = {
            "title": book_obj.Title,
            "author": book_obj.Author,
            "genres": book_obj.Genre,
            "description": book_obj.Description,
            "image_url": book_obj.Cover_url,
            "pub_year": book_obj.Publish_year,
            "rating": book_obj.Rating,
            "rating_count": book_obj.Rating_Count,
        }
        return render(request,"Book_Detail_Page/book_detail.html",book_details)
