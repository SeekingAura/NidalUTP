from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
@csrf_exempt
def useRecognotion(request):
	if(request.method == 'GET'):
		print("hey se hizo GET", request.GET)
		for key in request.GET:
			print(key)
			value = request.GET[key]
			print(value)
		#print(request.REQUEST['section'])
		# request.method.get.POST("")
		"""
		# create a Dejavu instance
		djv = Dejavu(config)

		# Fingerprint all the mp3's in the directory we give it
		# djv.fingerprint_directory("mp3 prueba", [".mp3"]


		# Recognize audio from a file
		results = djv.recognize(FileRecognizer, sys.argv[1])
		confidenceOverall=0
		for result in results:
			confidenceOverall+=result.get("confidence")


		resultsOverall={}

		## only name of birds, production mode
		for result in results:
			if(result.get("song_name").split("-")[0] in resultsOverall):
				resultsOverall[result.get("song_name").split("-")[0]]+=result.get("confidence")
			else:
				resultsOverall[result.get("song_name").split("-")[0]]=result.get("confidence")
		
		print("data ->", resultsOverall)
		results=[]
		for result in sorted(resultsOverall.items(), key=lambda kv: kv[1], reverse=True):#order by value (number of confidences)
			print("ave {} se estima ser {:0.2f}%".format(result[0], (result[1]/confidenceOverall)*100))
			results.append([result[0], "{:0.2f}%".format((result[1]/confidenceOverall)*100)])
		"""

	if(request.method == 'POST'):
		print("hey se hizo post")
		for key in request.POST:
			print(key)
			value = request.POST[key]
			print(value)
		# request.method.get.POST("")
	return JsonResponse({'lista':"[['MelanerpesFormicivorus', '74.56%'], ['AramidesCajaneus', '8.77%'], ['SynallaxisBrachyura', '7.02%'], ['RupornisMagnirostris', '3.07%'], ['LepidocolaptesSouleyetii', '2.19%'], ['PheugopediusSclateri', '1.75%'], ['SynallaxisAzarae', '1.32%'], ['XiphorhynchusSusurrans', '0.88%'], ['DryocopusLineatus', '0.44%']]"})
# Create your views here.

