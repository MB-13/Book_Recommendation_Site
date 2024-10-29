from django.shortcuts import render
from django.views import View
from Home_Page.models import Book_Detail,Book_Detail_2,BestSeller

# Create your views here.
class HomeView(View):
    def get(self,request):
        bestseller = BestSeller.objects.all()
        top_500 = Book_Detail_2.objects.all().order_by("-weighted_avg")[:500]
        return render(request,"Home_Page/home.html",{"top_500":top_500,"bestseller":bestseller})