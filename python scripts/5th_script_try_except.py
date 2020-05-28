while True:
	try:
		x = int(input('Enter a valid number:'))
		break
	except ValueError:
		print('not a valid value')
	except EOFError:
		print('exit')
		break
	finally:
		print('\nPlease enter a valid number (not in characters)\n')