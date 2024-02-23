from django.http import HttpResponse
from django.shortcuts import render


def show(response):
    return render(response, 'analysis.html')
