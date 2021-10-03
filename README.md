# CS50_Lec3_Python_Django
CS50 Web programming course provided by Harvard University intro to Django web framework (Course notes)


CS50 Web programming course Harvard Uni Notes on Django Python framework 

python manage.py runserver
python manage.py startapp hello

#add the hello app to settings.py
#add def index in views.py in hello folder

#add urls a path to hello views httpresponse.


#adding other apps to the project
python manage.py startapp NAME

adding static with css requires restart to server

inheritance by adding a layout.html to use similar html instead of copy and pasting multiple html files
this html file (layout) is based on the index html file where body is differnt
##{% extends 'tasks/layout.html' %}
##{%block body %}


when adding urls in django be careful of namespace collisions e.g multiple of same names in urls (index)

for this we add a app_name in urls.py called tasks then back in the add.html we add the name 'tasks' followed by a colon with the name 'index'
url 'tasks:index'

when dealing with sessions
python manage.py migrate
