def create_counter(n):
	print('create_counter()')
	while True:
		yield n
		print('increment n')
		n += 1
