# Karbordhaye method constructor?
# -------------------------------

from datetime import datetime

class Person:
	''' __doc__
	author: Mahdi.
	email: mahdi@uga.edu.
	'''
	thisCount = 0;  # This is a Class variable.

	def __init__(self, name):  
		self.name = name  # This is an instance variable.
		self.birth = datetime.now()

		print('\n'+name+' is created on '+ str(self.birth),'.\n')
		Person.thisCount += 1
		
	def thisFunctionName(self, name):
		print(name)
		
	def __del__(self):
		print(self.name,' destroyed')

if __name__ == '__main__':  # Module besurate dasti ejra shode.
	
	Mahdi = Person('Mahdi')
	print('Mahdi.birth:', Mahdi.birth)
	
##	2 Attribute ee ke har object dare:

##	__doc__
##   In hamun tozihate dakhele __doc__ hast.

##   obj.__module__
##	__main__

#	print('Mahdi.__module__:', Mahdi.__module__,'\n')
	
#	print('Mahdi.__dict__:', Mahdi.__dict__,'\n')

## __name__ ru kelas tarif mishe na object.
#	print("Person.__name__:",Person.__name__)
	
## __bases__
#	print("Person.__bases__:", Person.__bases__)
	
## __ Garbage Collection ==> Happening by python. --> we can define a method name Distructor. It can show you a message when the object is removing.

# a = 1
# b = a
# id(a)
# id(b)  # Same as a. Now we have two different variables which are pointing to the same amount.
# del(a)
# We do not have the arrow from a to 1 any more.
# If I say del(b) there is no a and b.
# Now python will figure out that we have an object with no use!
