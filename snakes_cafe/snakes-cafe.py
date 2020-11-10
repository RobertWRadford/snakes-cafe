menuItems = {
	'Wings': 0,
	'Cookies': 0,
	'Spring Rolls': 0,
	'Salmon': 0,
	'Steak': 0,
	'Meat Tornado': 0,
	'A Literal Garden': 0,
	'Ice Cream': 0,
	'Cake': 0,
	'Pie': 0,
	'Coffee': 0,
	'Tea': 0,
	'Unicorn Tears': 0,
}

response = ''

print('**************************************\n**    Welcome to the Snakes Cafe!   **\n**    Please see our menu below.    **\n**                                  **\n** To quit at any time, type "quit" **\n**************************************\n\nAppetizers\n----------\nWings\nCookies\nSpring Rolls\n\nEntrees\n-------\nSalmon\nSteak\nMeat Tornado\nA Literal Garden\n\nDesserts\n--------\nIce Cream\nCake\nPie\n\nDrinks\n------\nCoffee\nTea\nUnicorn Tears\n')

while response != 'Quit':
	print('***********************************\n** What would you like to order? **\n***********************************')
	response = input('> ').title()
	if response != 'Quit':
		if response in menuItems:
			menuItems[response]+=1
			quantity = 'orders have' if menuItems[response] > 1 else 'order has'
			print(f'** {menuItems[response]} {quantity} of {response} been added to your meal **')
		else:
			print(f'** Apologies but we don\'t sell {response} here. **')
print('** Your order is as follows: **')
for item in menuItems:
	if menuItems[item] > 0:	
		print(f'{menuItems[item]} {item}')
print('** End of your order. **')
