from django.urls import path
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as view_django
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('delete/<int:pk>', views.post_delete, name='post_delete'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('accounts/login/', view_django.LoginView.as_view(), name='login'),
    path('accounts/logout/', view_django.LogoutView.as_view(next_page='/'), name='logout'),

]