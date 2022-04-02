from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response

from .models import Library_Books
from .serializers import BookSerializers

import joblib


# Create your views here.

def imageView():
    pass

class bookList(APIView) :
    def __init__(self):
        pass
    def post(self , request):
        bookName = str(self.request.data['bookName'])
        bookAuthor = str(self.request.data['bookAuthor'])
        dateCreated = str(self.request.data['dateCreated'])
        price = int(self.request.data['price'])
        availability = bool(self.request.data['availability'])
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.data , status=404)

    def get(self,request):
        Books = Library_Books.objects.all()
        serializer = BookSerializers(Books, many=True)
        return Response(serializer.data)


