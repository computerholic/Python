# Karbordhaye method constructor?
# -------------------------------

from datetime import datetime  # Ino man import mikonam ta betoonam ba object datetime kar konam.
# Onject zaman ro mikham azash estefade konam.

class Person:
	'''
	author: Mahdi.
	email: mahdi@uga.edu.
	'''

	# Different methods have different names due to their responsibilities. One of them is constructor which we make an object that method happens!
	def __init__(self, name):  # Initialize.  # This is the constructor method. and as usual we should pass it the self.
		self.name = name
		self.birth = datetime.now()
		print('Human is created on',str(self.birth))

	def thisFunctionName(self, name):
		print(name)  # Har tabe besoorate pishfarz None ro bar migardoone.

if __name__ == '__main__':  # Module besurate dasti ejra shode.
	obj1 = Person('Mahdi')  # Making an instance from an object.

# ----------------------- Attributes -----------------------------------
# print(dir(obj))  # We can see which attributes it have. 

# How can I add attribute to a Class?
# obj.name = 'Ali'
# dir(obj)
# So I can add attribute to it.
