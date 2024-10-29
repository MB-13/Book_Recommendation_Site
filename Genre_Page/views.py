from django.shortcuts import render
from django.views import View
from Home_Page.models import Book_Detail,Book_Detail_2

from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.

class GenreView(View):
    def get(self,request,genre):
        if genre == "All Books":
            genre_book_list = Book_Detail_2.objects.all().order_by("id")   
        else:
            genre_book_list = Book_Detail.objects.filter(Genre=genre.lower()).order_by('id')
        
        paginator = Paginator(genre_book_list,20)  # Show 10 books per page
        page_number = request.GET.get('page',1)
        page_obj = paginator.get_page(page_number)
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            books_data = list(page_obj.object_list.values('id','Title','Cover_url'))
            return JsonResponse({
                'books':books_data,
                'has_next': page_obj.has_next()
            })
        
        return render(request,"Genre_Page/genre.html",{"genre":genre,'page_obj':page_obj})

# class BookListView(View):
#     def get(self, request, genre):
#         # Filter books based on the genre
#         book_list = Book_Detail.objects.filter(Genre=genre.lower())  # Adjust according to your model
#         paginator = Paginator(book_list, 30)  # Show 10 books per page
#         page_number = request.GET.get('page', 1)
#         page_obj = paginator.get_page(page_number)

#         if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#             books_data = list(page_obj.object_list.values('id', 'title', 'Cover_url'))  # Adjust fields as necessary
#             return JsonResponse({'books': books_data, 'has_next': page_obj.has_next()})

#         return JsonResponse({'books': [], 'has_next': False})  # Handle non-AJAX requests gracefully