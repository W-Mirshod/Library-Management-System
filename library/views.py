from rest_framework import generics, status
from rest_framework.response import Response
from .models import Books
from .serializers import BookSerializer


class BookListAPIView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        if 'status' not in self.request.data:
            serializer.save(status='in_stock')
        else:
            serializer.save()

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
