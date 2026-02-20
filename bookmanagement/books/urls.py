from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', LoginView.as_view(template_name='books/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('', views.book_list, name='book_list'),
    path('add', views.book_create, name='book_add'),
    path('edit/<int:id>/', views.book_update, name='book_edit'),
    path('delete/<int:id>/', views.book_delete, name='book_delete'),
]