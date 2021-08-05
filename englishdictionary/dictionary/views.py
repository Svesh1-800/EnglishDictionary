from django.shortcuts import render
from django.http import HttpResponse


def index(self):
    return HttpResponse("Hello")