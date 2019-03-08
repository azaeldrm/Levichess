from levichess.mainfiles.piece import Piece
from levichess.mainfiles.moverules import MoveRules


class Knight(Piece):
	"""description of class"""
	def __init__(self,colorID,numberID):
		Piece.__init__(self,colorID,2)
		self.piecetype = 'KNIGHT' + ' ' + str(numberID)
		self.numberID = numberID

	def MoveType(self,yf,xf):
		yi, xi = self.Location
		ny = yf - yi
		nx = xf - xi
		if MoveRules.Lshape(yi, xi, yf, xf, ny, nx) == True:
			return True
		else:
			return False

	def KillType(self,yf,xf):
		if self.MoveType(yf,xf) == True:
			return True
		else:
			return False
