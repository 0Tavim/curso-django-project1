from django.http import HttpResponse
from django.shortcuts import render

# from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html')


def main(request):
    return HttpResponse('MAIN PAGE 1')
