from django.core.management.base import BaseCommand
from my_app.models import City, Profession, Vacancy

class Command(BaseCommand):
    help = 'Удаление всех данных из базы данных'

    def handle(self, *args, **kwargs):
        confirmation = input("Вы уверены, что хотите удалить все данные? (да/нет): ")
        if confirmation.lower() != 'да':
            self.stdout.write(self.style.WARNING('Удаление данных отменено.'))
            return
        
        Vacancy.objects.all().delete()
        Profession.objects.all().delete()
        City.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Все данные успешно удалены!'))