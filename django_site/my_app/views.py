from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.shortcuts import render
from .models import Vacancy
from .forms import VacancyForm
from django.urls import reverse

# Create your views here.

def main_view(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'my_app/index.html', context={'vacancies' : vacancies})


def show_vacancy(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    return render(request, 'my_app/vacancy.html', context={'vacancy': vacancy})


def create_vacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_app:index'))
        else:
            return render(request, 'my_app/create.html', context={'form': form})
    else:
        form = VacancyForm()
        return render(request, 'my_app/create.html', context={'form': form})
    

def show_contact(request):
    return render(request, 'my_app/contact.html')