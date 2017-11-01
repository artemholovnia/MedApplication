from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.

MAX_DATE = datetime.strptime('2000-12-31', '%Y-%m-%d')
MIN_DATE = datetime.strptime('1950-01-01', '%Y-%m-%d')

class Permission(models.Model):
    user = models.ForeignKey(User, default = 0)
    permission_name = models.CharField(max_length = 30, verbose_name = 'Permission', blank = True, null = True, default = 'User')
    add_content = models.BooleanField(blank = True, null = False, verbose_name = 'Add content', default = 0 )
    change_content = models.BooleanField(blank = True, null = False, verbose_name = 'Change content', default = 0 )
    delete_content = models.BooleanField(blank = True, null = False, verbose_name = 'Delete content', default = 0 )

    def __str__(self):
        return '%s' % (self.permission_name)

class Client(models.Model):
    user = models.ForeignKey(User, default= 1)
    name = models.CharField(max_length=20, verbose_name = 'Имя')
    sorname = models.CharField(max_length=20, verbose_name = 'Фамилия')
    number = models.CharField(max_length=20, verbose_name = 'Номер телефона',)
    birthday = models.DateField(default=MAX_DATE.strftime('%Y-%m-%d'), verbose_name='День рождения')
    info = models.TextField(max_length = 100, blank = True, null = True, default = None, verbose_name = 'Дополнительно')
    token = models.CharField(max_length = 32, default = 'admin_url', verbose_name = 'Токен')
    registration_date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name = 'Дата регистрации')
    status = models.IntegerField(blank=True, null=True, default=0, verbose_name='Статус клиента')


    def __str__(self):
        return '%s %s' % (self.name, self.sorname)

    class Meta():
        ordering = ['-registration_date']

class Usluga(models.Model):
    title = models.CharField(max_length = 30, verbose_name = 'Название процедуры')
    user = models.ForeignKey(User, default= 1)
    token = models.CharField(max_length = 8, default = 'admin_url_service', verbose_name = 'Токен')
    def __str__(self):
        return '%s' % (self.title)
    class Meta():
        ordering = ['title']

class UslugaDlaClienta(models.Model):
    foreign_key = models.ForeignKey(Client)
    title = models.ForeignKey(Usluga)
    user = models.ForeignKey(User, default = 1)
    date = models.DateField(default = datetime.today().strftime('%Y-%m-%d'), verbose_name = 'Дата процедуры')
    time = models.TimeField(verbose_name = 'Время процедуры', null=True, blank=True)
    cash = models.IntegerField(blank = True, null = False, default = 0, verbose_name = 'Цена')
    income = models.IntegerField(blank = True, null = False, default = 0, verbose_name= 'Заработок')
    medicine = models.CharField(max_length = 30, verbose_name = 'Название препарата', null = True, blank = True, default = None)
    info = models.TextField(max_length=100, verbose_name='Дополнительно', null = True, blank = True, default = None)
    token = models.CharField(max_length=8, default='admin_url', verbose_name='Токен')
    #image_from = models.ImageField(upload_to='/images/', null=True)
    #image_to = models.ImageField(upload_to='/images/', null=True)
    class Meta():
        ordering = ['-date']
