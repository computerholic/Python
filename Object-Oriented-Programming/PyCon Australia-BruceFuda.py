# Example: an inventory/ pack.

# What do all packs have in common?

# They store things:
# - Capacity.
# - Add things to them.
# - Remove things from them.

# These things define the class.

# -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- *
# Not all packs are the same:
# - Some are bigger than others.
# - Different colours/ materials.

# Differences are reflected in object details.

class Pack:
	''' A standard game character inventory.'''
	
	def __init__(self,capacity):
		''' constructs an empty pack object. '''
		self.capacity = capacity
		self.content = []

	def add_Item(self, item):
		''' Adds an item to the pack. '''
		
		if isinstance(item, Weapon):
			if not self.is_full() and self.space_left() >= item.size:
				self.content.append(item)
				print(item.name + 'has been added to your Pack')
				return True
			else:
				print('You do not have space for ' + item.name)
		else:
			print('You cannot put that into your pack.')
		return False
		
class Item:
	
	''' Defines the Item superclass '''
	def __init__(self, name, size):
		''' Instantialates an Item object '''
		self.name = name
		self.size = size
	
	def __str__(self):
		pass
		
class Weapon(Item):  # Weapons are items. But they have extra features that apply to all weapons. The weapon class inherits Item.
	''' Defines the weapon object '''
	
	def __init__(self, name, size, power):
		''' Instantiates a Weapon object '''
		super().__init__(name, size)
		self.power = power
	
	def __str__(self):
		''' String representation of Weapon '''
	return super().__str__() + 'and power' + str(self.power)  # In chizie ke dare be ers mire.
	
	def swing(self):
		pass
		
class Food(Item):
	''' Defines the Food class'''
	
	def __init__(self, name, size, potency):-
	
	def __str__(self):
		pass
	
	def eat(self):
		pass
	
if __name__ == '__main__':
		
	my_pack = Pack(20)
	my_large_pack = Pack(50)
	my_tiny_Pack = Pack(5)
	
	my_sword = Weapon('Sword', 12, 20)
	my_sabre = Weapon('Sabre', 9, 16)
	my_steak = Food('Steak', 1,10)
	
	print("Packs are ready!")
		
		
