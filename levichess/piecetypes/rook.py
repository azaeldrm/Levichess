from levichess.mainfiles.piece import Piece
from levichess.mainfiles.moverules import MoveRules


class Rook(Piece):
	"""Rook is awesome"""
	def __init__(self,colorID,numberID):
		Piece.__init__(self,colorID,1)
		self.piecetype = 'ROOK' + ' ' + str(numberID)
		self.numberID = numberID

	def MoveType(self,yf,xf):
		yi, xi = self.Location
		ny = yf - yi
		nx = xf - xi
		if ny != 0 and nx == 0:
			if MoveRules.Vertical(yi, xi, yf, xf, ny) == True:
				print('Vertical: True')
				return True
		elif nx != 0 and ny == 0:
			if MoveRules.Horizontal(yi, xi, yf, xf, nx) == True:
				print('Horizontal: True')
				return True
		else:
			return False

	def KillType(self,yf,xf):
		if self.MoveType(yf,xf) == True:
			return True
		else:
			return False
