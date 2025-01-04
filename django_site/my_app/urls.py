from my_app import views
from django.urls import path

app_name = 'my_app'

urlpatterns = [
    path('', views.main_view, name="index"),
    path('vacancy/<int:id>/', views.show_vacancy, name='vacancy'),
    path('create-vacancy/', views.create_vacancy, name='create-vacancy'),
    path('contact/', views.show_contact, name='contact')
]