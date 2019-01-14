from ChessBoard import ChessBoard


class ChessGame:
	gameBoard = []
	def init_game():
		ChessBoard.init_board(ChessBoard.gameBoard)
		ChessBoard.start_board(ChessBoard.gameBoard)
