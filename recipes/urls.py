from django.urls import path

from recipes.views import home, main

urlpatterns = [
    path('', home),
    path('home/', main),
]
