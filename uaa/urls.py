from django.urls import path
from . import views

#paths for account app.
urlpatterns = [
    path('',views.LoginView, name='login_url'),
    path('register/',views.RegisterView, name="register_url"),
    path('dashboard/',views.DashboardView, name='dashboard_url'),
    
    path('profile/',views.ProfileView, name='profile_url'),
    path('allUsers/',views.AllUsersView, name='allUsers_url'),
]