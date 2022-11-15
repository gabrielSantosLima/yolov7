class Piece:

	def __init__(self, x, y, x2, y2, name):
		self.top_left = (x, y)
		self.bottom_left = (x, y2)
		self.top_right = (x2, y)
		self.bottom_right = (x2, y2)
		self.height = y2 - y
		self.width = x2 - x
		self.name = name

