from Piece import Piece
from MoveRules import MoveRules

class Bishop(Piece):
	"""description of class"""
	def __init__(self,colorID,numberID):
		Piece.__init__(self,colorID,3)
		self.piecetype = 'BISHOP' + ' ' + str(numberID)
		self.numberID = numberID

	def MoveType(self,yf,xf):
		yi, xi = self.Location
		if MoveRules.Diagonal(yi, xi, yf, xf, 0) == True:
			return True
		else:
			return False

	def KillType(self,yf,xf):
		if self.MoveType(yf,xf) == True:
			return True
		else:
			return False