from django.urls import path, include
from django.contrib import admin
from . import views,staffview,studentview


staffpattern = [
    path('profile',staffview.Profile,name="profile"),
    path('createclass',staffview.ClassCreateView.as_view(),name="createclass"),
    path('updateclass/<int:pk>',staffview.ClassUpdateView.as_view(),name="updateclass"),

]

studentpattern = [
  
    path('joinclass',studentview.AddClass,name="joinclass"),
    path('deleteclass/<str:classname>',studentview.DeleteView,name="removeclass")


]





pattern = [
    path('camera', views.editor),
    path("register",views.register),
   
    path('url/<str:name>',views.getMeetUrl),
    path('classes/<str:classname>',views.AllClasses,name="classes"),
    path('seturl/',views.setMeetUrl),
    path('unseturl/',views.UnsetMeetUrl),
    path('user/<str:email>',views.checkUser),
    path('settime',views.PostTiming,name="posttime"),
    path('details/<int:pk>',views.CalculateTime,name="details"),
    path("chart/<int:pk>",views.population_chart,name="chart"),
]

urlpatterns = studentpattern + staffpattern +pattern

