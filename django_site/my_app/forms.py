from django import forms
from .models import Vacancy, Tag


class VacancyForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Vacancy
        fields = ['profession', 'city', 'salary', 'description']
        
        
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']