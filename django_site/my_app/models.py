from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Profession(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Vacancy(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name='vacancies')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='vacancies')
    salary = models.FloatField()

    def __str__(self):
        return f"{self.profession.name} in {self.city.name} salary {self.salary}"  
