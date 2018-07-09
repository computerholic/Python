# Karbordhaye method constructor?
# -------------------------------

from datetime import datetime

class Person:
	'''
	author: Mahdi.
	email: mahdi@uga.edu.
	'''
	thisCount = 0;  # This is a Class variable.

	def __init__(self, name):  
		self.name = name  # This is an instance variable.
		self.birth = datetime.now()

		print(str(name)+' is created on '+ str(self.birth),'.')
		Person.thisCount += 1
		
	def thisFunctionName(self, name):
		print(name)

if __name__ == '__main__':  # Module besurate dasti ejra shode.
	
	Mahdi = Person('Mahdi')
	print('Person.count: ',Person.thisCount)
	print('Mahdi.name',Mahdi.name)
	
	Mahdi.phone = '7063868110'  # Add an attribute to Mahdi! Now if you dir(Ali)
	print(dir(Mahdi))
	
	del Mahdi.phone  # Remove Mahdi's attribute.
	print(dir(Mahdi))
	
	Maryam = Person('Maryam')
	print('Person.count: ',Person.thisCount)
	print('Maryam.name: ',Maryam.name)
	
	


# -------------------- Naming the Class variables.

# Copy funtions.
# the first word small. the rest are big.
# --------------------- Class Variable ---------------------------------
# Moteghayeri ke makhsuse Class e ! va azun olgue sakhte mishe.


# ----------------------- Attributes -----------------------------------
# print(dir(obj))  # We can see which attributes it have. 

# How can I add attribute to a Class?
# obj.name = 'Ali'
# dir(obj)
# So I can add attribute to it.


