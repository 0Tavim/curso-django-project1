from django.urls import path

from recipes.views import home, main

urlpatterns = [
    path('', main),
    path('home/', home),
]
