from django.db import models

from django.contrib.auth.models import AbstractUser

STATUS = (
    ("Новое", "Новое"),
    ("Приянт", "Приянт"),
    ("Откланено", "Откланено"),
)

class User(AbstractUser):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    surname = models.CharField(max_length=254, verbose_name='Фамилия', blank=False)
    patronymic = models.CharField(max_length=254, verbose_name='Отчество', blank=True)
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False)
    email = models.CharField(max_length=254, verbose_name='Почта', unique=True, blank=False)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона', blank=True)
    role = models.CharField(max_length=254, verbose_name='Роль',
                            choices=(('admin', 'Администратор'), ('user', 'Пользователь')), default='user')

    USERNAME_FIELD = 'username'

    def full_name(self):
        return ' ' .join([self.name, self.surname, self.patronymic])

    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=6)
    body = models.TextField()
    tags = models.CharField(choices=STATUS, blank=True, null=True, max_length=40, default="Новое")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title