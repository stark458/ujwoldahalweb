# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:15:58 2020

@author: Lenovo
"""
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name = 'index')]


