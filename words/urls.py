from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.custom_logout, name='logout'),
    path('', views.WordListView.as_view(), name='word-list'),
    path('word/<int:pk>/', views.WordDetailView.as_view(), name='word-detail'),
    path('trainer/', views.trainer, name='trainer'),
    path('edit/', views.edit_words, name='edit-words'),
    path('add/', views.add_word, name='add-word'),
    path('edit/<int:id>/', views.edit_word, name='edit-word'),
    path('delete/<int:id>/', views.delete_word, name='delete-word'),
    path('register/', views.register, name='register'),
    path('api/words/', views.WordAPIList.as_view(), name='api-word-list'),
    path('api/words/<int:pk>/', views.WordAPIDetail.as_view(), name='api-word-detail'),
]