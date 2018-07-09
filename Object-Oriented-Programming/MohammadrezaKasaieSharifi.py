class ClassName:  # Always ClassName! All start with Capital.
	'''
	author: Mahdi.
	email: mahdi@uga.edu.
	'''
	
	def thisFunctionName(self, name):  # Always pass the self as an input.
		print(name)  # Har tabe besoorate pishfarz None ro bar migardoone.

if __name__ == '__main__':  # Module besurate dasti ejra shode.
	obj1 = ClassName()  # Making an instance from an object.
	print(obj1.thisFunctionName('this is my name.'))  # Baraye function ee ke roye sheye object1 ejra mishe . mizarim.	


# Note 2: har function ruye yek object ejra mishe!
# Class avale har kalame bayad bozorg bashe! for function this is different:
# thisFunctionName(self).
