class Piece:

	def __init__(self, x, y, x2, y2, name):
		self.top_left = x
		self.top_right = x2
		self.bottom_left = y
		self.bottom_right = y2
		self.width = self.top_right - self.top_left
		self.height = self.top_left - self.bottom_left
		self.name = name

