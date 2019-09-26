#!source ./env/bin/activate
import warnings
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
import os
import sys

import fnmatch

from pydub import AudioSegment

config = {
"database": {
	"host": "127.0.0.1",
	"user": "root",
	"passwd": "cidt", 
	"db": "avesscheme"
}
}

# Easy way to get properly name of birds from DB
birdList=[
	'Aramides Cajaneus', 'Nyctidromus Albicollis',
	'Aulacorhynchus Haematopygus', 'Pheugopedius Sclateri',
	'Dryocopus Lineatus', 'Pionus Menstruus',
	'Grallaria Guatimalensis', 'Pitangus Sulphuratus',
	'Hafferia Immaculata', 'Rupornis Magnirostris',
	'Henicorhina Leucosticta', 'Synallaxis Azarae',
	'Lepidocolaptes Souleyetii', 'Synallaxis Brachyura',
	'Megascops Choliba', 'Thamnophilus Atrinucha',
	'Melanerpes Formicivorus', 'Thamnophilus Multistriatus',
	'Momotus Aequatorialis', 'Turdus Ignobilis',
	'Myiodynastes Maculatus', 'Xiphorhynchus Susurrans'
]


def find_files(path, extensions):
		# Allow both with ".mp3" and without "mp3" to be used for extensions
		extensions = [e.replace(".", "") for e in extensions]

		for dirpath, dirnames, files in os.walk(path):
				for extension in extensions:
						for f in fnmatch.filter(files, "*.%s" % extension):
								p = os.path.join(dirpath, f)
								yield (p, extension)

if __name__ == '__main__':
	


	# Recognize audio from a file
	#
	runFile=False
	testMode=False

	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{}" "filename"\n'.format(sys.argv[0]))
		raise SystemExit(1)#termina el programa
	
	

	# create a Dejavu instance
	djv = Dejavu(config)

	# Open csv file for data recolection
	# Must be granted first line with file_name, bird_name, percentage_result, confidence_file, confidence_overall\n
	

	# Open files with extension .mp3 from folder test
	for fileName, fileExtension in find_files(sys.argv[1],["mp3"]):
		# Format print for separate print results on terminal
		print("-"*30)

		print(fileName)

		# Open any audio file
		sound = AudioSegment.from_file(fileName)

		# Set sample rate in 44100
		sound= sound.set_frame_rate(44100)

		# Set number of channels in 2
		sound = sound.set_channels(2)

		# Rename file with properly extension
		fileName=fileName.replace("."+fileExtension, ".mp3")
		
		# Create audio file with respective settings (same file is overwrite)
		sound.export(fileName, format="mp3", bitrate="192k")
		
		# Rename file with spaces
		# print(fileName.split(" "))
		# folderTest, folderBird, filePath=fileName.split("/")
		# name1, name2, number=filePath.split(" ")
		# os.system("mv {} {}".format("'"+fileName+"'", "'"+folderTest+"/"+folderBird+"/"+name1+" "+name2+"-"+number.lower()+"'"))

		# Get respective name of bird
		birdName=fileName.split("/")[2].split("-")[0].title()

		if(birdName in birdList):
			# Get all confidences from analysis
			results = djv.recognize(FileRecognizer, fileName)
			resultsOverall={birdName:0}
			confidenceOverall=0
			for result in results:
				# Sum all Confidences
				confidenceOverall+=result.get("confidence")

				if(result.get("song_name").split("-")[0] in resultsOverall):
					resultsOverall[result.get("song_name").split("-")[0]]+=result.get("confidence")
				else:
					resultsOverall[result.get("song_name").split("-")[0]]=result.get("confidence")
			
			
			

			# Open file
			csvFile=open("Stadistical Dejavu-Bird.csv", "a", encoding="utf-8")

			# Case if confidences are none (very noise audio)
			if(confidenceOverall==0):
				for key in resultsOverall:
					print("ave {}, porcentaje {}%, confidences {}".format(key, 0, resultsOverall.get(key)))
			
				csvFile.write("{}, {}, {}, {}, {}\n".format(fileName, birdName, 
				0, resultsOverall.get(birdName), confidenceOverall
			))
			else:
				for key in resultsOverall:
					print("ave {}, porcentaje {}%, confidences {}".format(key, 
						(resultsOverall.get(key)/confidenceOverall), resultsOverall.get(key)
						)
					)
			
				csvFile.write("{}, {}, {}, {}, {}\n".format(fileName, birdName, 
				(resultsOverall.get(birdName)/confidenceOverall), resultsOverall.get(birdName), confidenceOverall
			))

			# Close file
			csvFile.close()
		else:
			print("ERROR, not found name of bird in DB with file {}, probably dont have a correct \
				format to read on system Dejavu-Bird or name of bird are not write correct".format(fileName))

		# Format print for separate results on terminal
		print("-"*30)
						

	# resultsOverall={}
	# testMode=False

	# sound = AudioSegment.from_file(request.FILES['ionicfile'].temporary_file_path())
	# sound= sound.set_frame_rate(44100)
	# sound = sound.set_channels(2)
	# sound.export(request.FILES['ionicfile'].temporary_file_path(), format="mp3", bitrate="198k")