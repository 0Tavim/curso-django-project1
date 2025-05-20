from django.http import HttpResponse

# from django.shortcuts import render


def home(request):
    return HttpResponse('HOME PAGE 1')


def main(request):
    return HttpResponse('MAIN PAGE 1')
