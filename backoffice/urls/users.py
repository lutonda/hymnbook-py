"""hymnbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.urls import include,  path
from backoffice.views import users as views

urlpatterns = [
        path('',views.list),
        path('new', views.new),
        path('update',views.update)
]
