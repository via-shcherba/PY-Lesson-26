from my_app import views
from django.urls import path

app_name = 'my_app'

urlpatterns = [
    path('', views.main_view, name="index"),
    path('vacancy/<int:id>/', views.show_vacancy, name='vacancy'),
    path('create-vacancy/', views.create_vacancy, name='create-vacancy'),
    path('contact/', views.show_contact, name='contact'),
    path('tag-list', views.TagListView.as_view(), name='tag_list'),
    path('tag-detail/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('tag-create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tag-update/<int:pk>/', views.TagUpdataView.as_view(), name='tag_update'),
    path('tag-delete/<int:pk>/', views.TagDeleteView.as_view(), name='tag_delete')
]