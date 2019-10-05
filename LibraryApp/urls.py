from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.front,name="front"),
    path('form/',views.form, name="form"),
    path('login/', views.login_view, name="login"),
    path('admin/', views.admin,name="admin"),
    path('studentadmin/', views.studentadmin, name="studentadmin"),
    path('student/',views.student,name="student"),
    path('book/',views.book, name="book"),
    path('search/', views.search, name="search"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('bookform/', views.bookform, name="bookform"),
    path('editbook/<int:id>/', views.editbook, name="editbook"),
    path('bookavailable/',views.bookavailable, name="bookavailable"),
    path('order/',views.order, name="order"),
    path('history/',views.history, name='history'),
    path('fine/',views.fine, name='fine'),
    path('logout/',views.log_out, name="logout")
   ]