class ClassName:
	'''
	author: Mahdi.
	email: mahdi@uga.edu.
	'''
	# Different methods have different names due to their responsibilities. One of them is constructor which we make an object that method happens!
	def __init__(self):
		print('Object is created')
	
	
	def thisFunctionName(self, name):
		print(name)  # Har tabe besoorate pishfarz None ro bar migardoone.

if __name__ == '__main__':  # Module besurate dasti ejra shode.
	obj1 = ClassName()  # Making an instance from an object.
