from tastypie.authentication import ApiKeyAuthentication


# Создаем аутентификации для всех классов кроме метода Get
class CustomAuthentication(ApiKeyAuthentication):
    # kwargs - все именнованые аргументы будут добавлены в словарь kwargs
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True  # Просто возвращаем тру и не выполняем аутентификацию

        # Вызываем метод из родительского класса
        return super().is_authenticated(request, **kwargs)
