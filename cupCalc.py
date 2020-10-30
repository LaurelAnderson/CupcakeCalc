#This is a cupcake price calculator

class CupcakeModel: 
	
	def __init__(self): 
		self.start()
		
	def start(self): 
		#start of the application
		print("This is a cupcake price calculator")

		final = round(choco_cup(), 2)
	 
		print("Final price is: ")
		print("$" + str(final))
		

	def choco_cup(self): 

		flour_price = float(input("Input the price per lb of flour: "))
		cocoa_price = float(input("Input the price per oz of cocoa powder: "))
		sugar_price = float(input("Input the price per lb of sugar: "))
		eggs_price = float(input("Input the price per dozen eggs: "))
		mayo_price = float(input("Input the price per oz of mayo: "))
		
		##The final flour is calculated by the taking the price per lb dividing it by the number 			##of cups in a lb (4.28) and multiplying that by the cups required. 
		flour_final = (2/(4.28)) * flour_price
		
		##The final cocoa is found by taking the price per oz of cocoa, multiplying by the number 			##of oz in a cup (8), and multiplying it by the recipe about (3/4 cup)
		cocoa_final = 6 * cocoa_price
		
		##Calculate the price for sugar by dividing the price per lb of sugar by the cups in a lb 			##(2). Thenmultiply by the cups needed (2)
		sugar_final = sugar_price
		
		##Calculate the price for eggs by taking the price per dozen eggs and multiplying it by 1/6
		eggs_final = (1/6) * eggs_price
		
		##Clalculate mayo in a similar way
		mayo_final = 8 * mayo_price
		
		return flour_final + cocoa_final + sugar_final + eggs_final + mayo_final


	
