from django.shortcuts import render
from django.http import HttpResponse
from django_ratelimit.decorators import ratelimit



@ratelimit(key='ip', rate='50/h')
def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")