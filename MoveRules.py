class MoveRules:
	"""description of class"""
	# Vertical Movement
	# n determines forward or backwards

	def Vertical(yi, xi, yf, xf, n):
		if (yf == yi + n) and (xf == xi):
			return True
		else:
			return False

	def Horizontal(yi, xi, yf, xf, n):
		if (yf == yi) and (xf == xi + n):
			return True
		else:
			return False

	def Diagonal(yi, xi, yf, xf, n):
		if abs(yf - yi) == abs(xf - xi):
			return True
		else:
			return False

	def Lshape(yi, xi, yf, xf, ny, nx):
		if (abs(ny) == 2 and abs(nx) == 1) or (abs(ny) == 1 and abs(nx) == 2):
			return True
		else:
			return False





