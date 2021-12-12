import requests
import unittest
import json
from faker import Faker
from random import randint 
import time

fake = Faker() 

userName = fake.user_name()
password = fake.password()
userID = randint(1, 1000)
firstName = fake.first_name()
lastName = fake.last_name()
email = fake.email()
phone = fake.phone_number()
userStatus = randint(1, 2)

print(userName)
print(password)
print(email)
print(phone)

# userName = 'hobbit'
# password = '123456789'
# userID = 12
# firstName =  'Samwise'
# lastName = 'Gamgee'
# email = 'modest_guy@shir.org'
# phone = 'no_phone'
# userStatus = 1

headers = {'Content-Type': 'application/json'}

class PostmanTests1(unittest.TestCase):

	def test_1_get_logIn(self):
		print('1')
		payload = json.dumps({'username': userName, 'password': password})
		response = requests.get('https://petstore.swagger.io/v2/user/login', headers = headers, params = payload)
		self.assertEqual(response.status_code, 200)
		time.sleep(10)

	def test_2_post_createUser(self):
		print('2')
		payload = json.dumps({'id': userID, 'username': userName, 'firstName': firstName, 'lastName': lastName, 'email': email, 'password': password, 'phone': phone, 'userStatus': userStatus})
		response = requests.post('https://petstore.swagger.io/v2/user', headers = headers, data = payload)
		print('request1: ' + response.request.body)
		self.assertEqual(response.status_code, 200)
		time.sleep(20)

	def test_3_get_checkCreating(self):
		print('3')
		response = requests.get('https://petstore.swagger.io/v2/user/'+ userName)
		print('response1: ' + response.text)
		self.assertEqual(response.status_code, 200)
		time.sleep(10)

# userName1 = 'brave_hobbit'
# password1 = '35464687'
# email1 = 'winner@shir.org'
# phone1 = '3546568768'

# userName1 = fake.user_name()
# password1 = fake.password()
# email1 = fake.email()
# phone1 = fake.phone_number()

userName = fake.user_name()
password = fake.password()
email = fake.email()
phone = fake.phone_number()

class PostmanTests2(unittest.TestCase):		

	def test_4_put_updateUser(self):
		print('4')
		payload = json.dumps({'id': userID, 'username': userName, 'firstName': firstName, 'lastName': lastName, 'email': email, 'password': password, 'phone': phone, 'userStatus': userStatus})
		response = requests.put('https://petstore.swagger.io/v2/user/'+ userName, headers = headers, data = payload)
		print('request2: ' + response.request.body)
		self.assertEqual(response.status_code, 200)
		time.sleep(20)

	def test_5_get_checkUpdating(self):
		print('5')
		response = requests.get('https://petstore.swagger.io/v2/user/'+ userName1)
		print('response2: ' + response.text)
		self.assertEqual(response.status_code, 200) 
		time.sleep(10)	

	def test_6_delete_deleteUser(self):
		print('6')
		response= requests.delete('https://petstore.swagger.io/v2/user/'+ userName1)
		self.assertEqual(response.status_code, 200)
		time.sleep(10)

	def test_7_get_checkAfterDeletion(self):
		print('7')
		response = requests.get('https://petstore.swagger.io/v2/user/'+ userName1)
		self.assertEqual(response.status_code, 404)
		time.sleep(10)		

		
if __name__ == '__main__':
	unittest.main()