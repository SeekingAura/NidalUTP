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
	if(request.method == 'GET'):
		print("hey se hizo GET")
		#print(request.REQUEST['section'])
		# request.method.get.POST("")

	if(request.method == 'POST'):
		print("hey se hizo post")
		# request.method.get.POST("")
	return JsonResponse({'mystring':"[['MelanerpesFormicivorus', '74.56%'], ['AramidesCajaneus', '8.77%'], ['SynallaxisBrachyura', '7.02%'], ['RupornisMagnirostris', '3.07%'], ['LepidocolaptesSouleyetii', '2.19%'], ['PheugopediusSclateri', '1.75%'], ['SynallaxisAzarae', '1.32%'], ['XiphorhynchusSusurrans', '0.88%'], ['DryocopusLineatus', '0.44%']]"})
# Create your views here.

