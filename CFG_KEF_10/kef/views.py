from django.shortcuts import render

from .models import Book
from django.template import loader
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def indexView(request):
    books = Book.objects.all()
    return render(request, "kef/index.html", {"books": books})
