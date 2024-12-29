from tastypie.authentication import ApiKeyAuthentication


#Создаем аутентификации для всех классов кроме метода Get
class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs): #kwargs - все именнованые аргументы будут добавлены в словарь kwargs
        if request.method == 'GET':
            return True # Просто возвращаем тру и не выполняем аутентификацию

        return super().is_authenticated(request, **kwargs) #Вызываем метод из родительского класса