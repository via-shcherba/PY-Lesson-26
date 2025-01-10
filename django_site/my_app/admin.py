from django.contrib import admin
from .models import City, Profession, Vacancy, Tag
# Register your models here.

def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)
    
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['profession', 'city', 'salary', 'description', 'is_active']
    actions = [set_active]
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    actions = [set_active]
    
admin.site.register(City)
admin.site.register(Profession)
admin.site.register(Tag, TagAdmin)
admin.site.register(Vacancy, VacancyAdmin)