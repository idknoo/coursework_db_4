from django.urls import path

from customer import views

app_name = 'customer'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/edit_passport', views.profile_edit_passport, name='profile_edit_passport'),
    path('logout/', views.auth_logout, name='logout'),
]
