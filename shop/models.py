from django.db import models
from django.utils import timezone
# В этом файле создаются модели для работы с БД, модель это интерфейс для взаимодействия с БД

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now) #Для этого поля дата генерируется автоматически

    def __str__(self):
        return self.title

class Courses(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    students_qt = models.IntegerField()
    reviews_qt = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
# on_delete=models.CASCADE означает что при удалении категории, будет удалены все курсы в бд