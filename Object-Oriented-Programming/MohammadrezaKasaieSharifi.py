# Karbordhaye method constructor?
# -------------------------------

from datetime import datetime

class Test:
	
class Person:
	''' __doc__
	author: Mahdi.
	email: mahdi@uga.edu.
	'''
	thisCount = 0;

	def __init__(self, name):  
		self.name = name
		self.birth = datetime.now()

		print('\n'+name+' is created on '+ str(self.birth),'.\n')
		Person.thisCount += 1
		
	def thisFunctionName(self, name):
		print(name)
		
	def __del__(self):
		print(self.name,' destroyed')
		
class ItMan(Person):  # In az ki bayad ers bari kone ? Az Person! # Hamamun esm darimo. Tarikh tavalod darimo ...
	
	def __init__(self, name, email):
		self.name = name
		self.email = email
	
	

if __name__ == '__main__':
	
	
	jadi = ItMan('Jadi', 'jadijadi@gmail.com')
	
	
	print('jadi.name:', jadi.name)
	print('jadi.email:',jadi.email)

#	print('jadi.birth:', jadi.birth)
	
#  To python mige harchandta mikhay Class dashte bash. Object mitune az chandta ers bebare!
#  Bazi zabana ye Class bozorg tush darim bad umade tike tikash karde. :-)
