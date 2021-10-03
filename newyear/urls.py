from django.urls import path
from . import views
#when someone just views this app run the defauly path function index
urlpatterns = [
    path('',views.index, name="index"),#.index is the name of the function
]
