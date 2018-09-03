##################################################################################
##################################################################################
# Program: Point of sales (POS) system
#
# Purpose: POS system for Young Chow Cafe
#
# Usage: python pos.py
##################################################################################
##################################################################################


if __name__ == '__main__':

	exit_flag = False
	main_menu = {}
	main_menu['1'] = 'Open new ticket'
	main_menu['2'] = 'Ticket lookup'
	main_menu['3'] = 'Void ticket'
	main_menu['4'] = 'Management'
	
	while not exit_flag:
		options = main_menu.keys()
		options.sort()


		print 'MAIN MENU'
		for entry in options:
			print entry, main_menu[entry]
		main_menu_selection = raw_input('Awaiting main menu selection: ')
		
		if main_menu_selection == '1':		# open new ticket
			# carryout, dine-in, delivery?
			# enter items
			# paid or unpaid?
		elif main_menu_selection == '2':	# ticket lookup
		elif main_menu_selection == '3':	# void ticket
		elif main_menu_selection == '4':	# management menu
		else:								# catch for invalid input
			print 'Invalid input!'