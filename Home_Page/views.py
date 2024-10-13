from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,"Home_Page/home.html")
    
class HomeView(View):
    def post(self,request):
        return render(request,"Home_Page/home.html")