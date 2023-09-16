from django.urls import path
from . import views
urlpatterns=[path('k/',views.fun,name="fun"),
             path('kk/',views.login,name="login"),
             path('ll/',views.home,name="home"),
             path('',views.logout,name="logout"),
             ]