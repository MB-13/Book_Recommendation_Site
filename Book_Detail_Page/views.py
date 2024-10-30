from django.shortcuts import render
from django.views import View
# Create your views here.

class DetailView(View):
    def get(self,request):
        return render(request,"Book_Detail_Page/book_detail.html")