def syntax():

	letters = ['A','B','C','D','E','F','G','H']
	numbers = [1,2,3,4,5,6,7,8]
	syntax1 = []
	syntax2 = []
	syntax = []

	for i in range(8):
		for j in range(8):
			for k in range(8):
				syntax1.append('move ' + letters[i] + str(numbers[j]) + ' to ' + letters[i] + str(numbers[k]))
			syntax2.append(letters[i] + str(numbers[j]))

	syntax.extend(syntax1)
	syntax.extend(syntax2)
	return syntax