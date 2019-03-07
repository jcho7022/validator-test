import re
import os
import json
from uuid import UUID
from datetime import datetime

def validate_entry(fe):
	try:
		return is_valid_timestamp(fe["ts"]) and is_valid_uuid(fe["si"]) and is_valid_uuid(fe["uu"]) and \
		is_valid_uuid(fe["bg"]) and is_valid_sha256(fe["sha"]) and is_valid_filename(fe["nm"]) and \
		is_valid_dp(fe["dp"]) and check_filename_path_match(fe["ph"], fe["nm"])
	except:
		return False
	
def is_valid_timestamp(timestamp):
	try:
		datetime.utcfromtimestamp(int(timestamp))
		return True
	except:
		return False

def is_valid_uuid(uuid_to_test):
	try:
		uuid_obj = UUID(uuid_to_test)
		return str(uuid_obj) == uuid_to_test
	except:
		return False

def is_valid_pt(pt):
	return pt >= 0
	
def is_valid_sha256(hash):
	return re.match("[a-z0-9]+", hash) != None and len(hash) == 64
	
def is_valid_dp(dp):
	return dp == 1 or dp == 2 or dp == 3
	
def is_valid_filename(filename):
	# invalid characters in a filename are \/:?"<>|
	return re.match('^[^/\:?"<>|]+$', filename) != None

def check_filename_path_match(filepath, filename):
	_, fn = os.path.split(filepath)
	return fn == filename
		