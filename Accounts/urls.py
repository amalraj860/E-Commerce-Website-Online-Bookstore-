from django.urls import path
from . import views

urlpatterns = [

    path('', views.Login, name='login'),
    path('register/', views.Register),
    path('logout',views.Logout,name='logout')

]
