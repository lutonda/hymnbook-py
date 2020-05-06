"""hymnbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.urls import include,  path
#from backoffice import views

urlpatterns = [
        #path('',views.backoffice_list_user),
        #path('new', views.backoffice_new_user),
        #path('update',views.backoffice_update_user),

    path('users/',include('backoffice.urls.users'))
]
