from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.front,name="front"),
    path('login/', views.login, name="login"),
    path('student/', views.student,name="student")
   ]