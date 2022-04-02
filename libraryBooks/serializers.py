from rest_framework import serializers

from .models import Library_Books

class BookSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Library_Books
        fields = '__all__'