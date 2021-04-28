from django.urls import path
from django.contrib import admin
import task.views as views

urlpatterns = [
    path("getapi", views.get),
    path("postapi", views.post),
    path("deleteapi", views.delete),
    path("completeapi", views.markcompleted),
    path("comptskdelapi", views.delcomptasks),
]
