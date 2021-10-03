from django.urls import path

from . import views
#app_name defaul django variablle name ??
app_name="tasks"
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add')
]
