# Karbordhaye method constructor?
# -------------------------------

from datetime import datetime  # Ino man import mikonam ta betoonam ba object datetime kar konam.
# Onject zaman ro mikham azash estefade konam.

class Person:
	'''
	author: Mahdi.
	email: mahdi@uga.edu.
	'''
	thisCount = 0;  # This is constant in all of the objects.

	def __init__(self, name):  
		self.name = name
		self.birth = datetime.now()

		print(str(name)+' is created on '+ str(self.birth),'.')
		Person.thisCount += 1 # count = count + 1 ==> Error. Age mikhay az moteghayeri too class estefade koni 

	def thisFunctionName(self, name):
		print(name)  # Har tabe besoorate pishfarz None ro bar migardoone.

if __name__ == '__main__':  # Module besurate dasti ejra shode.
	obj1 = Person('Mahdi')
	print('Person.count: ',Person.thisCount)
	obj2 = Person('Maryam')
	print('Person.count: ',Person.thisCount)


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


