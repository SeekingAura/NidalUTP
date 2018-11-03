from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse



def useRecognotion(request):
    if(request.method == 'POST'):
        print("hey se hizo post")
    return JsonResponse({'mystring':"return this string"})
# Create your views here.

