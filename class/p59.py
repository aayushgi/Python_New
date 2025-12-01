#printing of table using class
class table:

	
	def tab(self):
		num=int(input("enter the number which table did you want"))
		for i in range(1,11):
			print(num,"*",i,"=",num*i)
			
ft=table()
t=ft.tab()
   