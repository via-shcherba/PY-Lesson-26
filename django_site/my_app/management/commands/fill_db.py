from django.core.management.base import BaseCommand
from my_app.models import City, Profession, Vacancy

class Command(BaseCommand):
    help = 'Заполнение базы данных данными'

    def handle(self, *args, **kwargs):
        cities = ['Москва', 'Санкт-Петербург', 'Екатеринбург', 'Казань']
        for city_name in cities:
            City.objects.get_or_create(name=city_name)

        professions = ['Программист', 'Дизайнер', 'Аналитик', 'Менеджер']
        for profession_name in professions:
            Profession.objects.get_or_create(name=profession_name)

        vacancies = [
            {'profession': 'Программист', 'city': 'Москва', 'salary': 100000, 'description': 'Работа в офисе. Требуется опыт в продакшене от 3 лет'},
            {'profession': 'Дизайнер', 'city': 'Санкт-Петербург', 'salary': 80000, 'description': 'Ищем креативного опытного дизайнера в нашу команду'},
            {'profession': 'Аналитик', 'city': 'Екатеринбург', 'salary': 90000, 'description': 'Опыт в аналитике бизнеса обязателен.'},
            {'profession': 'Менеджер', 'city': 'Казань', 'salary': 70000, 'description': 'Опыт в управлении большими командами, стрессоустойчивость.'},
        ]

        for vacancy in vacancies:
            profession_obj = Profession.objects.get(name=vacancy['profession'])
            city_obj = City.objects.get(name=vacancy['city'])
            Vacancy.objects.get_or_create(
                profession=profession_obj,
                city=city_obj,
                salary=vacancy['salary'],
                description=vacancy['description']
            )

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена!'))