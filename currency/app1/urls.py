from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('index1',views.index1,name='index1')
]