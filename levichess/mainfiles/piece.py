class Piece:
	"""Piece class includes the attributes for all the pieces in the chess game.
	It also includes all the piece-types as its subclass."""

	def __init__(self,colorID,pieceID):
		self.colorID = colorID
		self.pieceID = pieceID
		self.isValid = True
		self.isAlive = True
		self.Location = [True,True]

		if colorID == 0:
			self.color = 'BLACK'
		elif colorID == 1:
			self.color = 'WHITE'

	def getPieceType(self):
		return self.piecetype

	def HowMove(self,yf,xf):
		return self.MoveType(yf,xf)

	def HowKill(self,yf,xf):
		return self.KillType(yf,xf)
