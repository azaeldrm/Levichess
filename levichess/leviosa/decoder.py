class Decoder:
	"""Class that translates board positions. Returns Objects that have the name of the Position. For instance A1 or C7"""
	def __init__(self):
		pass
		#self.whichPlayer = "0"

	def NameToLocation(string):
		#Defining a Turple: Turple are lists that cannot be modified. Turple = (a , b, c ,d)
		Letter = ('','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
		Number = ('','1', '2', '3', '4', '5', '6', '7', '8')

		try:
			CL = list(string)
			if (CL[0] in Letter) and (CL[1] in Number) == True:
				j = Letter.index(CL[0])
				i = Number.index(CL[1])
				return i, j
		except TypeError:
			print('TypeError: Please, input a String.')


	def LocationToName(y,x):
		#Defining a Turple: Turple are lists that cannot be modified. Turple = (a , b, c ,d)
		Letter = ('','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
		Number = ('','1', '2', '3', '4', '5', '6', '7', '8')
		try:
			Column = Letter[x]
			Row = Number[y]
			return Column + Row
		except TypeError:
			print('TypeError: Please, input ROW, COLUMN.')
