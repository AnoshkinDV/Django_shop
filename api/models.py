from tastypie.resources import ModelResource
from shop.models import Category, Courses
# Create your models here.
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


class CategoryResource(ModelResource):
    class Meta:  # Собственный атрибут класса CategoryResource
        queryset = Category.objects.all()  # Получаем все категории
        # Это имя будем указывать в пути при получении доступа к api
        resource_name = "categories"
        allowed_methods = ['get']  # Разрешенные http методы


class CourseResource(ModelResource):
    # Изменим этот класс
    class Meta:
        queryset = Courses.objects.all()
        resource_name = 'courses'
        # Разрешим пользователям создавать новые курсы и удалять
        allowed_methods = ['get', 'post', 'delete']
        # Включили авторизацию и аутентификацию для ресурса CourseResource
        # Добавили поля, которые не будут передаваться клиенту
        excludes = ['reviews_qt', 'created_at']
        authentication = CustomAuthentication()
        authorization = Authorization()
    # Hydrate преобразует входные данные в формат, подходящий для сохранения в базе данных.

    def hydrate(self, bundle):  # Эта функция позволяет вставить в объект category_id
        bundle.obj.category_id = bundle.data['category_id']
        return bundle
    # Dehydrate преобразует данные объекта модели в формат, удобный для отправки клиенту.

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle

    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()  # Теперь заголовки с большой
