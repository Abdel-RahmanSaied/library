from django.db import models

# Create your models here.

class Library_Books(models.Model):
    bookName = models.CharField(max_length=50)
    bookAuthor = models.CharField(max_length=50)
    dateCreated = models.DateField()
    price = models.IntegerField()
    availability = models.BooleanField(True)

    def __str__(self):
        return self.bookName





