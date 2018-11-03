#!source ./env/bin/activate
import warnings
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer
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
	##djv.fingerprint_directory("mp3", [".mp3"])
	#print("actual ->", os.getcwd()+chr(92)+"test")


	# Recognize audio from a file
	results = djv.recognize(FileRecognizer, sys.argv[1])
	confidenceOverall=0
	for result in results:
		confidenceOverall+=result.get("confidence")
	
	print ("Del archivo se ha reconocido:")
	for result in results:
		print ("ave {} se estima ser %{:0.2f}".format(
			result.get("song_name"),
			(result.get("confidence")/confidenceOverall)*100))

	# # Or recognize audio from your microphone for `secs` seconds
	# secs = 5
	# song = djv.recognize(MicrophoneRecognizer, seconds=secs)
	# if song is None:
	# 	print ("Nothing recognized -- did you play the song out loud so your mic could hear it? :)")
	# else:
	# 	print ("From mic with %d seconds we recognized: %s\n" % (secs, song))

	# # Or use a recognizer without the shortcut, in anyway you would like
	#recognizer = FileRecognizer(djv)
	#song = recognizer.recognize_file("test/asd.mp3")
	# print ("No shortcut, we recognized: %s\n" % song)