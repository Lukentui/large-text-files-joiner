import os
from time import time
from math import ceil

OUTPUT_FILE:str = "_latest.txt"
INPUT_DIR:str = "INPUT_TXT"
CHUNK_SIZE:int = 23046721 # = ~23mb

# methods
def prep_path(file:str) -> str:
	"""Return path to file"""

	return '%s\\%s' % (INPUT_DIR, file)

def read_in_chunks(file_object):
	"""Function for reading files chunk by chunk"""

	while True:
		data = file_object.read(CHUNK_SIZE)
		if not data:
			break
		yield data

#main code
START_AT:float = time()
print('YA EBAL TVOY MAT` STARTS HIS WORK!')
open(OUTPUT_FILE, 'w').close() # clear output file

# foreach files in INPUT_DIR
for file in os.listdir(INPUT_DIR):
	with open(prep_path(file), 'r', encoding="utf8", errors='ignore') as base_file:
		with open(OUTPUT_FILE, 'a', encoding="utf8", errors='ignore') as write_handler:
			chunk_num:int = 0
			chunks_total:int = ceil(os.path.getsize(prep_path(file))/CHUNK_SIZE)

			for chunk in read_in_chunks(base_file):
				chunk_num += 1
				write_handler.write(chunk) #append chunk to OUTPUT_FILE
				print("[CHUNKS %s/~%s]: %s" % (chunk_num, chunks_total, file))
			


	print("[READY]: %s" % file)
	print("------------------")
	print()

print()
print("JOINED IN: %s sec" % ceil(time()-START_AT))
