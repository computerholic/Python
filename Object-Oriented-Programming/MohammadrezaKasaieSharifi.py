# Private ? Public ? and hidden sazi chetoriast?

from datetime import datetime
from functools import total_ordering  # age esmesho ghable esme class benevisam va @ pass bedam in ye decoratore! yani age yekio neveshti baghiaro ham miare.

@total_ordering
class Test:
	test = 'Some string just to show that Class Test is working.'

class Person:
	''' __doc__
	author: Mahdi.
	email: mahdi@uga.edu.
	'''
	__thisCount = 0;

	def __init__(self, name, age):  
		self.name = name
		self.age = age
		self.birth = datetime.now()
		print('It was a Person.')

		print(name+' is created on '+ str(self.birth),'.\n')
		Person.__thisCount += 1

	def thisFunctionName(self, name):
		print(name, 'Called from class of Person.')

	def __del__(self):
		print(self.name,'destroyed.')
		print('He was a Person.')

	def __lt__(self, other):
		return self.age < other.age
		# Mahdi > Maryam

class ItMan(Person, Test):  # In az ki bayad ers bari kone ? Az Person! # Hamamun esm darimo. Tarikh tavalod darimo ...

	def __init__(self, name, email):
		self.name = name
		self.email = email
		print('He was an IT man :(.\n')

	def __del__(self):
		print(self.name,'destroyed.')
		print('He was an IT man :(.')

if __name__ == '__main__':

	jadi = ItMan('Jadi', 'jadijadi@gmail.com')	

	Mahdi = Person('Mahdi','24')
	Maryam = Person('Sara','23')

	print(1<3)
	print(Mahdi.age < Maryam.age)

	print()

# New Functions

# __gt__  >
# __lt__  <
# __eq__  ==
# __ne__  !=
# __ge__  >=
# __le__  <=

# 
