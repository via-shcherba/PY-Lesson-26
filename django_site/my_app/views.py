from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Vacancy, Tag
from .forms import VacancyForm, TagForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin

# Create your views here.

def main_view(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'my_app/index.html', context={'vacancies' : vacancies})


@user_passes_test(lambda u: u.is_superuser)
def show_vacancy(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    return render(request, 'my_app/vacancy.html', context={'vacancy': vacancy})


@login_required
def create_vacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('my_app:index'))
        else:
            return render(request, 'my_app/create.html', context={'form': form})
    else:
        form = VacancyForm()
        return render(request, 'my_app/create.html', context={'form': form})
    

def show_contact(request):
    return render(request, 'my_app/contact.html')


class NameContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Tags'
        return context
    
    
class TagListView(ListView, NameContextMixin):
    model = Tag
    template_name = 'my_app/tag_list.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.all()


class TagDetailView(UserPassesTestMixin, DetailView, NameContextMixin):
    model = Tag
    template_name = 'my_app/tag_detail.html'
    raise_exception = False

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        self.tag_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Tag, pk=self.tag_id)
    

class TagCreateView(LoginRequiredMixin, CreateView, NameContextMixin):
    form_class = TagForm 
    model = Tag
    success_url = reverse_lazy('my_app:tag_list')
    template_name = 'my_app/tag_create.html'

    def form_valid(self, form):
        return super().form_valid(form)
    
    
class TagUpdataView(UpdateView):
    fields = '__all__'
    model = Tag
    success_url = reverse_lazy('my_app:tag_list')
    template_name = 'my_app/tag_create.html'
    

class TagDeleteView(DeleteView):
    template_name = 'my_app/tag_delete_confirm.html'
    model = Tag
    success_url = reverse_lazy('my_app:tag_list')
