from django.urls import path
from .views import BookListAPIView, BookDetailAPIView

app_name = 'library'

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='details'),
]
