from . import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signin/create/', views.signin_create, name='create'),
]