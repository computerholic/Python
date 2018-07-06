print("========== God ========= \n\n")

class Employee:
	
	raise_amount = 1.04
	
	def __init__(self, first, last, pay):  #Constuction. #  Init method - Initialize. #Self is an instance.
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
	
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
		
	def apply_raise(self):
		self.pay = int(self.pay) * Employee.raise_amount  # 4 percent increasing rate.

# %% 
print("PART_0: \n")

emp_1 = Employee('Mahdi','Kashani','80000')
emp_2 = Employee('Maria Clare','Nunley','90000')

print(emp_1.email)
print(emp_2.email)

# %% 
print("PART_1: \n")

print(emp_1.first,emp_2.first)
Employee.fullname(emp_1)
print(emp_1.fullname())

# %%
print("PART_2: \n")

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# %%
print("\n")

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# %%
print(emp_1.__dict__)  # It gives us all of the attributes about emp_1.

# %%

# %%

# %%

# %%

# %%
