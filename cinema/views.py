from django.shortcuts import render
from .models import Movie
from .models import Genre
# Create your views here.

def home_page(request):
	return render(request, 'cinema/home_page.html',)
def search_page(request):
	return render(request, 'cinema/search_page.html',)