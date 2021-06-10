#importing libraries
import pandas as pd
import json

def read_data(filename):
	#initalising variables
	data = {}
	data['quotes'] = []
	count = 0

	# reading the csv file
	df = pd.read_csv (filename)

	#reading and putting values into data{}
	for itemList in df.values:
	    count += 1
	    data['quotes'].append({
	        'id': count,
	        'quote': itemList[0],
	        'author':itemList[1],
	    })

	write_data(data)

def write_data(data):
	# writing into an output file
	with open('data.json', 'w') as outfile:
	    json.dump(data, outfile)


if __name__ == '__main__':
	filename = 'data.csv'
	read_data(filename)