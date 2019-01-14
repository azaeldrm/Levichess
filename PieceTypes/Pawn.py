from Piece import Piece
from MoveRules import MoveRules

class Pawn(Piece):
	"""description of class"""
	def __init__(self,colorID,numberID):
		Piece.__init__(self,colorID,0)
		self.piecetype = 'PAWN' + ' ' + str(numberID)
		self.numberID = numberID

	def MoveType(self,yf,xf):
		yi, xi = self.Location
		n = yf - yi
		if abs(n) == 1:
			if self.colorID == 0:
				if MoveRules.Vertical(yi, xi, yf, xf, 1) == True:
					return True
				else:
					return False
			elif self.colorID == 1:
				if MoveRules.Vertical(yi, xi, yf, xf, -1) == True:
					return True
				else:
					return False
			else:
				return False
		else:
			return False

	
	def KillType(self,yf,xf):
		yi, xi = self.Location
		n = yf - yi
		if abs(n) == 1:
			if (self.colorID == 0) and (n>0) :
				if MoveRules.Diagonal(yi, xi, yf, xf, 1) == True:
					return True
				else:
					return False
			elif (self.colorID == 1) and (n<0):
				if MoveRules.Diagonal(yi, xi, yf, xf, -1) == True:
					return True
				else:
					return False
			else:
				return False
		else:
			return False