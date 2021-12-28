from os import name
from django.urls import path
#from django.urls.resolvers import URLPattern

from pages.views import  about, home, send, recieve, takenum,Average

urlpatterns = [
    path('',home),
    path('about/',about),
    path('send/',send),
    path('recieve/',recieve , name="recieve"),
    path('takenum/',takenum, name="takenum"),
    path('Average/',Average, name="Average"),
]