from tastypie.resources import ModelResource
from shop.models import Category, Courses
# Create your models here.
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication



class CategoryResource(ModelResource):
    class Meta: #Собственный атрибут класса CategoryResource 
        queryset = Category.objects.all() # Получаем все категории
        resource_name = "categories" #Это имя будем указывать в пути при получении доступа к api
        allowed_methods = ['get'] # Разрешенные http методы


class CourseResource(ModelResource):
    #Изменим этот класс
    class Meta:
        queryset = Courses.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get','post','delete'] # Разрешим пользователям создавать новые курсы и удалять
        #Включили авторизацию и аутентификацию для ресурса CourseResource
        authentication = CustomAuthentication()
        authorization = Authorization()
    #Hydrate преобразует входные данные в формат, подходящий для сохранения в базе данных.
    def hydrate(self, bundle): #Эта функция позволяет вставить в объект category_id
        bundle.obj.category_id = bundle.data['category_id']
        return bundle
    #Dehydrate преобразует данные объекта модели в формат, удобный для отправки клиенту.
    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category
        return bundle