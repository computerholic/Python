# Soal? Which __init__ ejra mishe?
# Overwrite kardan ya sarbar gozari?
# ----------------------------------------------------------------------

# Aval mibine Class __init__ dare ya na! Age dasht uno enjra mikone. Age nadasht mire
# unyekio negah mikone.
from datetime import datetime

class Test:
	test = 'Some string just to show that Class Test is working.'

class Person:
	''' __doc__
	author: Mahdi.
	email: mahdi@uga.edu.
	'''
	thisCount = 0;

	def __init__(self, name):  
		self.name = name
		self.birth = datetime.now()
		print('He was a Person.')

		print('\n'+name+' is created on '+ str(self.birth),'.\n')
		Person.thisCount += 1
		
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
	
	print('jadi.name:', jadi.name)
	print('jadi.email:',jadi.email)
	print('jadi.test:',jadi.test)
	print(Test.__bases__)  # in neshoon mide in class az kodum kelasa dare ers bari mikone. # Inheritance.
	
	Mahdi = Person('Mahdi')

#	print('jadi.birth:', jadi.birth)
	
#  To python mige harchandta mikhay Class dashte bash. Object mitune az chandta ers bebare!
#  Bazi zabana ye Class bozorg tush darim bad umade tike tikash karde. :-)
