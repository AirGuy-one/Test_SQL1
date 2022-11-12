from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('my/', views.my, name='my'),
    path('about/', views.about, name='about_url'),
    path('add/', views.add, name='add_url'),
    path('users/', views.users, name='users_url'),
    path('like/', views.like, name='like_url'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('some/', views.some),
    path('thisis/', views.user),
    path('set/', views.set),
    path('oauth/', views.auth),
    path('thisis1/', views.thisis)

]
