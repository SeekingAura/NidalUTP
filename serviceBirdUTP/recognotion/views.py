from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import warnings
warnings.filterwarnings("ignore")
import sys

sys.path.append('../')# Set parent of parent folder
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
import os
import sys


config = {
"database": {
	"host": "127.0.0.1",
	"user": "root",
	"passwd": "1234", 
	"db": "avesscheme"
}
}

def useRecognotion(request):
    if(request.method == 'POST'):
        print("hey se hizo post")
    return JsonResponse({'mystring':"return this string"})
# Create your views here.

