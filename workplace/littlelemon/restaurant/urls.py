from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_items:<int:pk>', views.display_menu_item, name="menu_item"),
]
"""
This module defines the URL patterns for the restaurant app.

The urlpatterns list contains the paths for different views in the app.
Each path is associated with a specific view function and has a unique name.

- The path '' (empty string) maps to the home view function.
- The path 'about/' maps to the about view function.
- The path 'book/' maps to the book view function.
- The path 'menu/' maps to the menu view function.
- The path 'menu_items:<int:pk>' maps to the display_menu_item view function.

These URL patterns are used by Django to route incoming requests to the appropriate view functions.
"""
