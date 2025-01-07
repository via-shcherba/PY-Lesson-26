from django.db import models
from django.utils import timezone

# Create your models here.

class TimeStamp(models.Model):
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class City(TimeStamp):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Profession(TimeStamp):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class Tag(TimeStamp):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name

class Vacancy(TimeStamp):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name='vacancies')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='vacancies')
    salary = models.FloatField()
    description = models.CharField(max_length=200, default=None)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.profession.name} in {self.city.name} salary {self.salary}"  