from django.urls import path
from . import views


urlpatterns = [
    path('',views.my_app,name='my_app'),
    path('new_search',views.new_search,name='new_search'),
]
