from django.urls import path
from . import views 
from .views import  BookDetailView, BookListView

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/new/', views.book_create, name='book_create'),
    path('book/<int:pk>/edit/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete', views.book_delete, name='book_delete'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail')
]