# Karbordhaye method constructor?
# -------------------------------

from datetime import datetime  # Ino man import mikonam ta betoonam ba object datetime kar konam.
# Onject zaman ro mikham azash estefade konam.

class Person:
	'''
	author: Mahdi.
	email: mahdi@uga.edu.
	'''
	count = 0;  # This is constant in all of the objects.
	
	def __init__(self, name):  
		self.name = name
		self.birth = datetime.now()
		
		print(str(name)+' is created on '+ str(self.birth),'.')
		Person.count += 1 # count = count + 1 ==> Error. Age mikhay az moteghayeri too class estefade koni 

	def thisFunctionName(self, name):
		print(name)  # Har tabe besoorate pishfarz None ro bar migardoone.

if __name__ == '__main__':  # Module besurate dasti ejra shode.
	obj1 = Person('Mahdi')
	print('Person.count: ',Person.count)
	obj2 = Person('Maryam')
	print('Person.count: ',Person.count)
	


# Mahdi 2018-07-09 00:23:33.350050
# Maryam 2018-07-09 00:23:33.350155
        
# --------------------- Class Variable ---------------------------------
# Moteghayeri ke makhsuse Class e ! va azun olgue sakhte mishe.


# ----------------------- Attributes -----------------------------------
# print(dir(obj))  # We can see which attributes it have. 

# How can I add attribute to a Class?
# obj.name = 'Ali'
# dir(obj)
# So I can add attribute to it.


