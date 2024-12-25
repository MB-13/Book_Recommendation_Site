from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
from django.http import JsonResponse
import uuid
from django.views import View
from Home_Page.models import Book_Detail,Book_Detail_2,BestSeller,BookembedModel
from login_and_signup.models import userInfo
from sentence_transformers import SentenceTransformer
from Search_Page.views import model
import numpy as np
from Search_Page.views import title_embeddings
from django.urls import reverse



# Create your views here.
class HomeView(View):
    def get(self,request):
        bestseller = BestSeller.objects.all()
        
        # print(user_id)
        top_500 = Book_Detail_2.objects.all().order_by("-weighted_avg")[:500]
        try:
            user_id = request.session.get('user_id')
            my_future_read = self.getMyList(user_id)
            user_recom_list = self.getUserRecom(user_id)
            user_recom_list = user_recom_list if len(user_recom_list) != 0 else bestseller
            return render(request,"Home_Page/home.html",{"top_500":top_500,"bestseller":bestseller,"my_future_read":my_future_read,"user_recom_books":user_recom_list})
        except:
            return HttpResponseBadRequest("You are not Logged In.....")
    
    def getMyList(self,user_id):
        user_id = uuid.UUID(user_id)
        User = userInfo.objects.get(userId=user_id)
        books_list = User.readLater.all()
        return books_list
    
    def getUserRecom(self,user_id):
        # getting user
        
        user_id = uuid.UUID(user_id)
        User = userInfo.objects.get(userId = user_id)
        if len(User.readLater.all()) == 0:
            return []
        book_embedding_array = np.matrix([BookembedModel.objects.get(Book=book).Embedding for book in User.readLater.all()])
        mean_embedding_array = np.mean(book_embedding_array,axis=0)
        simScore = model.similarity(mean_embedding_array,title_embeddings)
        simScore = simScore[0]
        enum_simscore = np.array(list(enumerate(simScore)))
        sorted_enum_simscore = sorted(enum_simscore,key=lambda x:x[1],reverse=True)
        user_recom_books = [Book_Detail_2.objects.get(book_id=y[0]) for y in sorted_enum_simscore[:108]]
        return user_recom_books

        
    
    
class AddFutureReadView(View):
    def get(self,request):
        # print(request.session.get('user_id'))
        user_id = request.session.get('user_id')
        if user_id:
            user_id = uuid.UUID(user_id)
            book_id = request.GET.get('q','')

            #getting book
            book = Book_Detail_2.objects.get(book_id=book_id)
            book_coverurl = book.Cover_url
            book_title= book.Title
            book_detail = {
                'book_id' : book_id,
                'book_coverurl' : book.Cover_url,
                'book_title' : book.Title
            }
            
            #getting user
            User = userInfo.objects.get(userId = user_id)
            if book not in User.readLater.all():
                User.readLater.add(book)
                return JsonResponse({'message':'Book Added','book_detail':book_detail})
            else:
                return ({'message':'Book already exist'})
        else:
            print("Not loggedd in")
            return HttpResponse("Not logged in",status=401)


class RemoveFutureReadView(View):
    def get(self,request):
        user_id = request.session.get('user_id')
        if user_id:
            user_id = uuid.UUID(user_id)
            book_id = request.GET.get('q','')

            #grtting book
            book = Book_Detail_2.objects.get(book_id = book_id)
            book_detail = {
                "book_id" : book_id
            }
            
            #getting user
            User = userInfo.objects.get(userId = user_id)
            User.readLater.remove(book)
            return JsonResponse({'message' : "Book removed from future reads!","book_detail":book_detail})
        else:
            return HttpResponse("Not logged in",status=401)
        
## ___ TO reset the session when clicked log out ____

class LogOutView(View):
    def get(self,request):
        try:
            del request.session["user_id"]
            request.session.flush()
            return JsonResponse({"message":"Logged Out Succesfully"})
        except:
            return JsonResponse({"message":"Error occured"})