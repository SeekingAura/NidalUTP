#!source ./env/bin/activate
import warnings
warnings.filterwarnings("ignore")

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

if __name__ == '__main__':
	if(len(sys.argv)!=2):#Verifica la cantidad de argumentos a la hora de compilar si no son 2. "py 'fichero.py' 'archivo'"
		sys.stderr.write('Usage: "{}" "filename"\n'.format(sys.argv[0]))#permite que al al compilar indique que debe de darse el archivo de la forma python.exe "fichero.py" "Archivo a abrir, como un simple print"
		raise SystemExit(1)#termina el programa
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
		"""
		for result in results:
			if(result.get("song_name").split("-")[0] in resultsOverall):
				resultsOverall[result.get("song_name").split("-")[0]]+=result.get("confidence")
			else:
				resultsOverall[result.get("song_name").split("-")[0]]=result.get("confidence")
		"""

	for result in sorted(resultsOverall.items(), key=lambda kv: kv[1], reverse=True):#order by value (number of confidences)
		print("ave {} se estima ser {:0.2f}%".format(result[0], (result[1]/confidenceOverall)*100))

