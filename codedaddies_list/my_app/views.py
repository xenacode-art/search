import requests
import re
from requests.compat import quote_plus
#from bs4 import BeautifulSoup
#from bs4.element import Tag
from .models import Search
from django.shortcuts import render

#page = requests.get(
 #   'https://forecast.weather.gov/MapClick.php?lat=41.884&lon=-87.6324#.XIRQYFNKgUE'
#)


def my_app(request):
 return render(request,'base.html')



def new_search(request):
 search = request.POST.get('search')
 print(search)
 stuff_for_frontend ={

     'search':search
      
 }
 return render(request, 'my_app/new_search.html', stuff_for_frontend)
