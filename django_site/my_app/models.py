from django.db import models
from django.utils import timezone
from usersapp.models import StandardUser

# Create your models here.

class ActiveManager(models.Manager):

    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)

class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True

class TimeStamp(models.Model):
    created = models.DateTimeField(default=timezone.now, verbose_name='Created Datetime')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated Datetime', db_index=True)

    class Meta:
        abstract = True

class City(TimeStamp):
    name = models.CharField(max_length=100, unique=True, verbose_name='Name')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        

class Profession(TimeStamp):
    name = models.CharField(max_length=100, unique=True, verbose_name='Name')
    
    def __str__(self):
        return self.name
    
class Tag(TimeStamp, IsActiveMixin):
    name = models.CharField(max_length=16, unique=True, verbose_name='Name')

    def __str__(self):
        return self.name

class Vacancy(TimeStamp, IsActiveMixin):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name='vacancies', verbose_name='Profession')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='vacancies', verbose_name='City')
    salary = models.FloatField(verbose_name = 'Salary')
    description = models.CharField(max_length=200, default=None, verbose_name='Description')
    tags = models.ManyToManyField(Tag, verbose_name = 'Tags')
    user = models.ForeignKey(StandardUser, on_delete=models.CASCADE, verbose_name='User')

    def __str__(self):
        return f"{self.profession.name} in {self.city.name} salary {self.salary}"  
    
    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'