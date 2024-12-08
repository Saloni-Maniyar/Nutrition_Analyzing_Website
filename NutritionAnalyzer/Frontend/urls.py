from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyze/', views.analyze, name='analyze'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]
