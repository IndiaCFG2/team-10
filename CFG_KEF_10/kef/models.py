from django.db import models

# Create your models here.
class Book(models.Model):
    # NICK NAME should be unique
    book_id = models.CharField(max_length=100, unique =  True)
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    about = models.CharField(max_length = 250)
    employee = models.CharField(max_length=150, null = True, blank = True)

    def __str__(self):
        return self.book_id
