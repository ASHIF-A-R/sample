choice = int(input("1.Addition\n2.Subtraction\n\nenter your choice : "))


def sum():

		#return a+b
		a = int(input("enter first value : "))
		b = int(input("enter second value : "))


		print("sum equal to = ",a+b)
		
def div():
		#return a-b
		a = int(input("enter first value : "))
		b = int(input("enter second value : "))

		print("Difference equl to = ", a-b)
		
		
if choice==1:
	sum()


elif choice==2:
	div()
	

else:
	print("Invalid Entry")
