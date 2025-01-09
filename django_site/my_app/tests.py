from django.test import TestCase
from .models import City, Profession, Vacancy, Tag
from usersapp.models import StandardUser
from faker import Faker
from mixer.backend.django import mixer


# Create your tests here.
class VacancyTestCase(TestCase):

    def setUp(self):
        self.city = City.objects.create(name='Minsk')   
        self.profession = Profession.objects.create(name='Developer') 
        self.tag = Tag.objects.create(name='python')
        user = StandardUser.objects.create_user(username='test_user', email='test@test.com', password='test1234567')
        self.vacancy = Vacancy.objects.create(profession=self.profession, city=self.city, user=user, salary=111, description='test description')
        self.vacancy.tags.add(self.tag)

    def test_city_str(self):
        self.assertEqual(str(self.city), 'Minsk')
        
    def test_profession_str(self):
        self.assertEqual(str(self.profession), 'Developer')
        
    def test_tag_str(self):
        self.assertEqual(str(self.tag), 'python')
        
    def test_vacancy_str(self):
        self.assertEqual(str(self.vacancy), 'Developer in Minsk salary 111')


class VacancyTestCaseFaker(TestCase):

    def setUp(self):
        faker = Faker()
        
        self.city = City.objects.create(name=faker.name())   
        self.profession = Profession.objects.create(name=faker.name()) 
        self.tag = Tag.objects.create(name=faker.name())
        user = StandardUser.objects.create_user(username=faker.name(), email='test@test.com', password='test1234567')
        self.vacancy = Vacancy.objects.create(profession=self.profession, city=self.city, user=user, salary=faker.random_int(min=100, max=1000), description=faker.words(nb=5))
        self.vacancy.tags.add(self.tag)
        
    def test_city_str(self):
        self.assertTrue(str(self.city))
        
    def test_profession_str(self):
        self.assertTrue(str(self.profession))

    def test_tag_str(self):
        self.assertTrue(str(self.tag))
    
    def test_vacancy_str(self):
        self.assertTrue(str(self.vacancy))


class VacancyTestCaseMixer(TestCase):

    def setUp(self):
        self.city = mixer.blend(City, name='San Francisco')
        self.profession = mixer.blend(Profession, name='Developer')
        self.tag = mixer.blend(Tag, name='remote')
        user = mixer.blend(StandardUser)
        self.vacancy = mixer.blend(Vacancy, profession=self.profession, city=self.city, salary=100000, description='Great job!', user=user)
                
    def test_city_str(self):
        self.assertEqual(str(self.city), self.city.name)
        
    def test_profession_str(self):
        self.assertEqual(str(self.profession), self.profession.name)
        
    def test_tag_str(self):
        self.assertEqual(str(self.tag), self.tag.name)
        
    def test_vacancy_str(self):
        expected_str = f"{self.vacancy.profession.name} in {self.vacancy.city.name} salary {self.vacancy.salary}"
        self.assertEqual(str(self.vacancy), expected_str)