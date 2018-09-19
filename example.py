import warnings
import json
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer
import os

# load config from a JSON file (or anything outputting a python dictionary)

config = {
"database": {
	"host": "127.0.0.1",
	"user": "root",
	"passwd": "97032609604cm", 
	"db": "avesscheme"
}
}

if __name__ == '__main__':

	# create a Dejavu instance
	djv = Dejavu(config)

	# Fingerprint all the mp3's in the directory we give it
	djv.fingerprint_directory("mp3", [".mp3"])
	#print("actual ->", os.getcwd()+chr(92)+"test")


	# Recognize audio from a file
	song = djv.recognize(FileRecognizer, "test/asd.mp3")
	print ("From file we recognized: %s\n" % song)

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