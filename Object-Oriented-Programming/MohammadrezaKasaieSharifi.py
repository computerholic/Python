# Karbordhaye method constructor?
# -------------------------------

from datetime import datetime  # Ino man import mikonam ta betoonam ba object datetime kar konam.
# Onject zaman ro mikham azash estefade konam.

class ClassName:
	'''
	author: Mahdi.
	email: mahdi@uga.edu.
	'''

	# Different methods have different names due to their responsibilities. One of them is constructor which we make an object that method happens!
	def __init__(self):  # Initialize.  # This is the constructor method. and as usual we should pass it the self.
		self.created = datetime.now()
		self.birth =
		
		print('Object is created')

	def thisFunctionName(self, name):
		print(name)  # Har tabe besoorate pishfarz None ro bar migardoone.

if __name__ == '__main__':  # Module besurate dasti ejra shode.
	obj1 = ClassName()  # Making an instance from an object.

print(datetime.now())
