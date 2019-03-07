import unittest
import file_entry_validator as fev
import json

class TestFileEntryValidator(unittest.TestCase):
	def test_is_valid_timestamp(self):
		# overflow should return false 
		self.assertFalse(fev.is_valid_timestamp(123123123123123123));
		# test valid timestamp
		self.assertTrue(fev.is_valid_timestamp(1551140352));

	def test_is_valid_uuid(self):
		# test invalid uuid
		self.assertFalse(fev.is_valid_uuid("123"));
		self.assertFalse(fev.is_valid_uuid("77c5423d-fbp9-4e4b-8270-b68e843301de"));
		
		# test valid uuid
		self.assertTrue(fev.is_valid_uuid("3380fb19-0bdb-46ab-8781-e4c5cd448074"));
		self.assertTrue(fev.is_valid_uuid("ecb1c882-472d-451c-a0ee-0bcc519957c6"));
		
	def test_is_valid_pt(self):
		# test invalid processing time
		self.assertFalse(fev.is_valid_pt(-1));
		# test valid processing time
		self.assertTrue(fev.is_valid_pt(1));
	
	def test_is_valid_sha256(self):
		# test valid sha256
		self.assertTrue(fev.is_valid_sha256("abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52"))
		# test invalid sha256(invalid @ character)
		self.assertFalse(fev.is_valid_sha256("@bb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52"))
		# test invalid sha256(invalid length)
		self.assertFalse(fev.is_valid_sha256("abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda5"))
		
	def test_is_valid_dp(self):
		# invalid disposition values 
		self.assertFalse(fev.is_valid_dp(0))
		self.assertFalse(fev.is_valid_dp(4))
		
		# valid disposition values
		self.assertTrue(fev.is_valid_dp(1))
		self.assertTrue(fev.is_valid_dp(2))
		self.assertTrue(fev.is_valid_dp(3))
		
	def test_is_valid_filename(self):
		self.assertTrue(fev.is_valid_filename("phkkrw"))
		self.assertFalse(fev.is_valid_filename("/phkkrw"))
		self.assertFalse(fev.is_valid_filename(":phkkrw"))
		self.assertFalse(fev.is_valid_filename(""))
	
	def test_check_filename_path_match(self):
		self.assertTrue(fev.check_filename_path_match("/efvrfutgp/expgh/phkkrw","phkkrw"))
		self.assertFalse(fev.check_filename_path_match("/efvrfutgp/expgh/phkkrw","phkkr"))
	
	def test_validate_entry(self):
		# valid json
		jo = json.loads(
		'{"ts":1551140352,"pt":62,"si":"5dd6dc22-4372-4687-a980-6aa24d03f68a",' + 
		'"uu":"abbd9199-6e08-48df-b834-48666921f1f2","bg":"b402487c-d960-4f5b-ae68-d78f61e218da",' +
		'"sha":"6d74ffc1ef8468de9c4556dd97f7005c095d202b3442722aedba1bd00e6754c5","nm":"ntoxyaoqv.zip",'+
		'"ph":"ntoxyaoqv.zip","dp":1}')			
		self.assertTrue(fev.validate_entry(jo))
		
		# invalid json
		jo = json.loads(
		'{"pt":62,"si":"5dd6dc22-4372-4687-a980-6aa24d03f68a",' + 
		'"uu":"abbd9199-6e08-48df-b834-48666921f1f2","bg":"b402487c-d960-4f5b-ae68-d78f61e218da",' +
		'"sha":"6d74ffc1ef8468de9c4556dd97f7005c095d202b3442722aedba1bd00e6754c5","nm":"ntoxyaoqv.zip",'+
		'"ph":"ntoxyaoqv.zip","dp":1}')			
		self.assertFalse(fev.validate_entry(jo))
	

if __name__ == '__main__':
	unittest.main()