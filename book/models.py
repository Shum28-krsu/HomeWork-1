from django.db import models


#HOMEWORK 2
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    about = models.TextField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    language = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='book_pictures/', null=True, blank=True)
    publisher = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title