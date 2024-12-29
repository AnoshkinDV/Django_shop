from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404
from .models import Courses
# Create your views here.
# Views - виды -  это контроллеры в паттерне MVC, связывают видимую часть приложения с моделями.
# Принимается request возвращает responce

def index(request):
    courses = Courses.objects.all()
    # return HttpResponse(''.join([str(course)+'<br>' for course in courses]))
    return render(request, 'shop/courses.html', {'courses':courses})


def single_course(request,courses_id): #courses_id берется из ссылки в веб-браузере
    #Option 1
    # try:    
    #     course = Courses.objects.get(pk=courses_id)
    #     return render(request,'shop/single_course.html',{'course':course})
    
    # except Courses.DoesNotExist: #Если нет курса в бд, то появляется ошибка
    #     raise Http404()

    #Option 2
    course = get_object_or_404(Courses,pk=courses_id)
    return render(request,'shop/single_course.html',{'course':course}) #Более короткий вариант
