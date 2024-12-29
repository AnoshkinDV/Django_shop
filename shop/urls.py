from django.urls import path
from . import views


app_name = 'shop'
#Маршрут для главной страницы приложения Shop
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:courses_id>', views.single_course, name='single_course')
]

