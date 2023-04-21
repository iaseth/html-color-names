from .utils import get_rgb_from_hex



class PyColor:
	def __init__(self, jo):
		self.name = jo["name"]
		self.hex = jo["code"]
		self.lowername = jo["name"].lower()
		self.rgb = get_rgb_from_hex(self.hex)

	def __str__(self):
		return f"PyColor '{self.name}' {self.rgb}"


