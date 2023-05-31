from django.urls import path
from home import views

urlpatterns = [
    path('feed/', views.feed, name="feed"),
    path('registration/', views.registration, name="registration"),
    path('', views.home, name="home"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('editprofile/', views.editprofile, name="editprofile" ), 
    path('addpost/', views.addpost, name="addpost"),
    path('editpost/<int:id>', views.editpost, name="editpost"),
    path('delete/<int:id>', views.delete, name="delete"),  
    path('views/<int:id>', views.views, name="views"),
    path('search/', views.search, name="search"),
    path('profile2/<int:pid>', views.profile2, name="profile2"),



]