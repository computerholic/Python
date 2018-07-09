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

		print('\n'+name+' is created on '+ str(self.birth),'.\n')
		Person.thisCount += 1
		
	def thisFunctionName(self, name):
		print(name)

if __name__ == '__main__':  # Module besurate dasti ejra shode.
	
	Mahdi = Person('Mahdi')
	print('Mahdi.birth:', Mahdi.birth)
	
	print()
	
# 	gettattr
	print("getattr(Mahdi, 'name': )", getattr(Mahdi, 'name'))
	print()
	
# 	setattr
	print("setattr(Mahdi, 'phone', '7063868110')", setattr(Mahdi, 'phone', '7063868110'))
	print()
	print(dir(Mahdi))
	
# 	hasattr
	print("", )
	print("hasatt(Mahdi, 'phone')? ", hasattr(Mahdi,'phone'))
	
# 	delattr
	print("delattr(Mahdi,'phone'): ",delattr(Mahdi,'phone'))
	print("hasatt(Mahdi, 'phone')? ", hasattr(Mahdi,'phone'))
	
# -------------------- 4 function that help us to manage the Class.

# getattr()  # get attribution.
# setattr()  # 

# -------------------- Naming the classVariables. ----------------------

# Copy funtions.
# the first word small. the rest are big.

# ----------------------- Attributes -----------------------------------
# print(dir(obj))  # We can see which attributes it have. 

# How can I add attribute to a Class?
# obj.name = 'Ali'
# dir(obj)
# So I can add attribute to it.


