import requests
import re
#from requests.compat import qoute_plus
#from bs4 import Beautifulsoup
#from bs4.element import Tag
#from .models import Search
from django.shortcuts import render

#page = requests.get(
 #   'https://forecast.weather.gov/MapClick.php?lat=41.884&lon=-87.6324#.XIRQYFNKgUE'
#)


def home(request):
 return render(request,'base.html')