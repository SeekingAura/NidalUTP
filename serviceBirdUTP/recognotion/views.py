from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.core.files.temp import NamedTemporaryFile
from django.core.files.temp import gettempdir
import requests
from contextlib import closing


import warnings
warnings.filterwarnings("ignore")
import sys

sys.path.append('../')# Set parent of parent folder
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
import os
import sys

from pydub import AudioSegment

# database dejavu system
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
	results=[]
	if(request.method == 'POST'):
		if("ionicfile" in request.FILES):
			sound = AudioSegment.from_file(request.FILES['ionicfile'].temporary_file_path())
			sound= sound.set_frame_rate(44100)
			sound = sound.set_channels(2)
			sound.export(request.FILES['ionicfile'].temporary_file_path(), format="mp3", bitrate="128k")

			djv = Dejavu(config)
			results = djv.recognize(FileRecognizer, request.FILES['ionicfile'].temporary_file_path())
			confidenceOverall=0
			for result in results:
				confidenceOverall+=result.get("confidence")


			resultsOverall={}
			testMode=False

			if(testMode):
			#full name of file, test mode
				for result in results:
					if(result.get("song_name") in resultsOverall):
						resultsOverall[result.get("song_name")]+=result.get("confidence")
					else:
						resultsOverall[result.get("song_name")]=result.get("confidence")
			else:
				## only name of birds, production mode
				for result in results:
					if(result.get("song_name").split("-")[0] in resultsOverall):
						resultsOverall[result.get("song_name").split("-")[0]]+=result.get("confidence")
					else:
						resultsOverall[result.get("song_name").split("-")[0]]=result.get("confidence")
			
			results=[]
			for result in sorted(resultsOverall.items(), key=lambda kv: kv[1], reverse=True):#order by value (number of confidences)
				## print result with Style
				#print("ave {} se estima ser {:0.2f}%".format(result[0], (result[1]/confidenceOverall)*100))
				results.append({result[0]:"{:0.2f}%".format((result[1]/confidenceOverall)*100)})
			
			# play recording (test)
			# os.system("ffplay {}".format(request.FILES['ionicfile'].temporary_file_path()))
	## show preview of JsonResult
	# print(results)
	return JsonResponse({'lista':str(results)})
# Create your views here.

