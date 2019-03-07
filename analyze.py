import json
import os
import file_entry_validator as fev

filestore = dict()
f = open("log.json", "r")
for line in f:
	try:
		file_entry = json.loads(line)
		filename, file_extension = os.path.splitext(file_entry["nm"])
		file_extension = file_extension.replace(".","")
		if file_extension != '' and fev.validate_entry(file_entry):
			if file_extension in filestore:
				filestore[file_extension].add(filename)
			else:
				filestore[file_extension] = set()
	except ValueError: 
		print('Decoding JSON has failed')


# print result
for key, value in filestore.items():
	print(key, len(value))
	

	

	