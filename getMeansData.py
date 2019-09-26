import os
import sys

import pandas as pd


if __name__=="__main__":
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $csvFileName $IndexOfX1\n'.format(sys.argv[0]))
		os._exit(1)

	if(".csv" in sys.argv[1]):
		data = pd.read_csv(sys.argv[1])
	
	# Replace All space in column headers
	data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)

    # get column headers such as [keyX1, keyX2, keyX3, ..., keyY]
	keyList=data.columns.values

	data=data.groupby(keyList[1]).agg({keyList[1]:"size", keyList[2]:"mean", keyList[3]:"mean", keyList[4]:"mean"}).rename(columns={keyList[1]:"count_songs", keyList[2]:keyList[2]+"_mean", keyList[3]:keyList[3]+"_mean", keyList[4]:keyList[4]+"_mean"})

	data.to_csv(sys.argv[1][:-4]+"_grouped"+sys.argv[1][-4:], index=True)