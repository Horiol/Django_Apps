# Django Music
This is a simple Django project that display a list of music genres. You are able to select any genre of the list to see all the songs that matches this genre and a chart (made using Google Charts) that show the average duration of each artist according to their songs in that genre.

## Overview
For this project I used [Django](https://www.djangoproject.com/) framework for both frontend and backend. Also, I used GitHub as a version control system ([GitHub repo](https://github.com/Horiol/Django_Apps)) and some other libraries and modules to make this app better and cooler, for example:
* [Bootstrap](http://getbootstrap.com/)
* [Graphos](https://github.com/agiliq/django-graphos)
* [Mathfilters](https://github.com/dbrgn/django-mathfilters)
* [DataTables](https://datatables.net/)

## Run project locally
* Clone the project
```bash
git clone git@github.com:Horiol/Django_Apps.git
```
* `cd` to directory
```bash
cd Django_Apps
```
* Install requirements
```bash
pip install -r requirements.txt
```
* Run server
```bash
python manage.py runserver

Then the application should be ready in <http://localhost:8000/>.
