from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home1, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/questions/', views.user_questions, name='user_questions'),
    path('profile/answers/', views.user_answers, name='user_answers'),
    path('profile/<int:user_id>/', views.other_user_profile, name='other_user_profile'),
    path('profile/<int:user_id>/questions/', views.other_user_questions, name='other_user_questions'),
    path('profile/<int:user_id>/answers/', views.other_user_answers, name='other_user_answers'),
]

