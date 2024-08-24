from django.db import models
from django.shortcuts import reverse


sex_choice = (
        ('мужской', 'мужской'),
        ('женский', 'женский'),
    )
'''категория'''
class Category(models.Model):
    title = models.CharField(max_length=32, verbose_name='категория')

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('category_list_url', kwargs={'pk': self.pk})

'''подразделение'''
class Division(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True, verbose_name='подразделение')
    address = models.CharField(max_length=240, blank=True, null=True, verbose_name='адрес')
    title_into_chaos = models.CharField(max_length=160, blank=True, null=True, verbose_name='название в запрос')
    outgoing = models.CharField(max_length=16, blank=True, null=True, verbose_name='исходящий')
    coming_from = models.DateField(default='2024-01-01', blank=True, null=True, verbose_name='исходящий от')

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('division_list_url', kwargs={'pk': self.pk})

 
'''ГЛАВНАЯ'''
class Person(models.Model):
    photo_card = models.ImageField(blank=True, null=True,
                                   upload_to='images/',
                                   default='images/default.jpg',
                                   verbose_name='фотокарточка',
                                   )
    personal_number = models.CharField(max_length=9,
                                       blank=True, null=True,
                                       verbose_name='личный номер',
                                       )
    last_name = models.CharField(max_length=16, verbose_name='фамилия')
    first_name = models.CharField(max_length=24, verbose_name='имя')
    patronymic = models.CharField(max_length=24, verbose_name='отчество', blank=True)
    date_of_birth = models.DateField(default='1983-08-08', verbose_name='дата рождения')
    sex = models.CharField(max_length=8, default='мужской', choices=sex_choice, verbose_name='пол')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1, blank=True, related_name='person_category')
    division = models.ForeignKey(Division, on_delete=models.PROTECT, default=1, blank=True, related_name='person_division')
    excluded = models.BooleanField(default=False, verbose_name='исключен')

    def __str__(self) -> str:
        return self.last_name
    
    def get_absolute_url(self):
        return reverse('person_detail_url', kwargs={'pk': self.pk})
 
""" Архив """
class Dismissed(models.Model):
    last_name = models.CharField(max_length=16, verbose_name='фамилия')
    first_name = models.CharField(max_length=24, verbose_name='имя')
    patronymic = models.CharField(max_length=24, verbose_name='отчество', blank=True)
    division = models.CharField(max_length=64, verbose_name='Подразделение')
    dismissed_from = models.DateField(verbose_name='уволен с', blank=True, null=True)
    order = models.CharField(max_length=64, blank=True, null=True, verbose_name='чей приказ')
    number = models.CharField(max_length=16, blank=True, null=True, verbose_name='номер приказа')
    an_order_from = models.DateField(verbose_name='приказ от', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('dismissed_person_url', kwargs={'pk': self.pk})
