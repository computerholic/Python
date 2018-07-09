# Private ? Public ? and hidden sazi chetoriast?

from datetime import datetime

class Test:
	test = 'Some string just to show that Class Test is working.'

class Person:
	''' __doc__
	author: Mahdi.
	email: mahdi@uga.edu.
	'''
	__thisCount = 0;

	def __init__(self, name):  
		self.name = name
		self.birth = datetime.now()
		print('He was a Person.')

		print('\n'+name+' is created on '+ str(self.birth),'.\n')
		Person.__thisCount += 1
		
	def thisFunctionName(self, name):
		print(name, 'Called from class of Person.')
		
	def __del__(self):
		print(self.name,'destroyed')
		print('He was a Person.')
		
		
class ItMan(Person, Test):  # In az ki bayad ers bari kone ? Az Person! # Hamamun esm darimo. Tarikh tavalod darimo ...
	
	def __init__(self, name, email):
		self.name = name
		self.email = email
		print('He was an IT man :(.')
	def __del__(self):
		print(self.name,'destroyed.')
		print('He was an IT man :(.')

if __name__ == '__main__':
	
	jadi = ItMan('Jadi', 'jadijadi@gmail.com')	
	Mahdi = Person('Mahdi')
	
	print("issubclass(ItMan, Person):?" ,issubclass(ItMan, Person) )
	print("isinstance(Mahdi, Person):?" ,isinstance(Mahdi, Person) )
	print("Person.__count:",Person.__thisCount)
	print("----------------------------------------------------------")
