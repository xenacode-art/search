from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
#    path('new-search/',views.new_search,new='new_search')
]