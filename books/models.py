from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pubished_date = models.DateTimeField()
    isbn_number = models.CharField(max_length=13)

    def __str__(self):
        return self.title
