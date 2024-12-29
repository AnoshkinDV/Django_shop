from django.apps import AppConfig


#Создание атрибутов классов, к ним обращаются через ShopConfig.name
class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
