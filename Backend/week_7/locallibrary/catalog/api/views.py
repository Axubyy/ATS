from rest_framework import generics
from .serializers import BookListSerializer, BookDetailSerializer
from ..models import Book, BookInstance


class BookListView(generics.ListCreateAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()
