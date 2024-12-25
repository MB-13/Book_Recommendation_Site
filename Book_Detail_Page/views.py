from django.shortcuts import render
from django.views import View
from Home_Page.models import Book_Detail_2,BestSeller,BookembedModel
# Create your views here.

class DetailView(View):
    def get(self,request,Id):
        book_obj = Book_Detail_2.objects.get(id=Id)
        recom_book_list = self.getRelated(book_obj)
        book_details = {
            "title": book_obj.Title,
            "author": book_obj.Author,
            "genres": book_obj.Genre,
            "description": book_obj.Description,
            "image_url": book_obj.Cover_url,
            "pub_year": book_obj.Publish_year,
            "rating": book_obj.Rating,
            "rating_count": book_obj.Rating_Count,
            "recom_book_list": recom_book_list,


        }
        return render(request,"Book_Detail_Page/book_detail.html",book_details)
    
    def getRelated(self,book_obj):
        book_embed_obj = BookembedModel.objects.get(Book=book_obj)
        simscore_list = book_embed_obj.SimScore
        enum_simscore_list = list(enumerate(simscore_list))
        sorted_enum_simscore_list = sorted(enum_simscore_list,key = lambda x:x[1],reverse=True)
        sorted_recom_index_list = [x[0] for x in sorted_enum_simscore_list]
        recom_book_list = [Book_Detail_2.objects.get(book_id=x) for x in sorted_recom_index_list[1:100]]
        return recom_book_list
    
class BestSelDetailView(View):
    def get(self,request,Id):
        book_obj = BestSeller.objects.get(id=Id)
        book_in_bd2 = Book_Detail_2.objects.get(Title=book_obj.Title)
        recom_book_list = DetailView.getRelated(self,book_in_bd2)
        book_details = {
            "title": book_obj.Title,
            "author": book_obj.Author,
            "genres": book_obj.Genre,
            "description": book_obj.Description,
            "image_url": book_obj.Cover_url,
            "pub_year": book_obj.Publish_year,
            "rating": book_obj.Rating,
            "rating_count": book_obj.Rating_Count,
            "recom_book_list": recom_book_list,
        }
        return render(request,"Book_Detail_Page/book_detail.html",book_details)
