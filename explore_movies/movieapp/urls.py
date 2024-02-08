from django.urls import path

from movieapp import views

urlpatterns = [
   path('',views.base,name='base'),
   path('login/', views.login, name='login'),
   path('register/', views.register, name='register'),
   path('movies/',views.movies,name='movies'),
   path('malayalam/', views.malayalam, name='malayalam'),
   path('english/', views.english, name='english'),
   path('hindi/', views.hindi, name='hindi'),
   path('watch/', views.watch, name='watch'),
   path('save/', views.save, name='save'),
   path('logout/', views.logout, name='logout')

]
