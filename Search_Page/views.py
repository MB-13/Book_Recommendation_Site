from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from sentence_transformers import SentenceTransformer
from .models import SearchEmbedModel
from Home_Page.models import Book_Detail_2
import numpy as np


model = SentenceTransformer("all-MiniLM-L6-v2")


def getTitleEmbed(title_df):
    query_set = title_df.objects.all()
    title_embed_list = np.matrix([book.TitleEmbed for book in query_set])

    return title_embed_list

def getTop6forquery(query_embed):
    
    sorted_enum_simscore = getSimScore(query_embed)
    top_6_sug_id = [y[0] for y in sorted_enum_simscore[:6]]
    return top_6_sug_id

def getSimScore(query_embed):
    query_embed = query_embed.astype(np.float64)
    simscore = model.similarity(query_embed,title_embeddings)
    simscore = simscore[0]
    enum_simscore = np.array(list(enumerate(simscore)))
    sorted_enum_simscore = sorted(enum_simscore,key=lambda x:x[1],reverse=True)
    return sorted_enum_simscore
    
title_embeddings = getTitleEmbed(SearchEmbedModel)



# Create your views here.
class SearchView(View):
    def get(self,request):
        return render(request,"Search_Page/search.html")
    
    

    
# route to get suggestions for search bar
class SearchSuggestionsView(View):
    def __init__(self):
        self.query_list = []

    def get(self,request):
        query = request.GET.get('q','')
        self.query_list.append(query)
        

        if query:
            query_embed = model.encode(self.query_list)
            numpy_query_embed = np.matrix(query_embed)
            suggest_index_list = getTop6forquery(numpy_query_embed)
            suggest_books = [Book_Detail_2.objects.get(book_id=x) for x in suggest_index_list]
            titles = [x.Title for x in suggest_books]
        
        return JsonResponse(titles, safe=False)
    

    

# route to get result for the books
class SearchResultView(View):
    def __init__(self):
        self.query_list = []

    def get(self,request):
        query = request.GET.get('q','')
        self.query_list.append(query)

        if query:
            query_embed = np.matrix(model.encode(self.query_list))
            enum_result_books = getSimScore(query_embed)
            result_indexes = [y[0] for y in enum_result_books[:207]]
            result_books_set = [Book_Detail_2.objects.get(book_id=p) for p in result_indexes]
            details = [(book.book_id,book.Cover_url,book.Title) for book in result_books_set]
        return JsonResponse(details,safe=False)


