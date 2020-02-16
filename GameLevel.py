from gameObject import *
from resourceManager import *
class GameLevel:
	def __init__(self):
		self.bricks = []

	def load(self, file, levelWidth, levelHeight):
		self.tile_data = []
		with open("level1.txt") as f:
			self.tile_data = [line.split() for line in f]

		self.init(self.tile_data, levelWidth, levelHeight)
			

	def init(self, tile_data, levelWidth, levelHeight):
		height = len(tile_data)
		width = len(tile_data[0])

		unit_width = levelWidth / width
		unit_height = levelHeight / height

		for y in range(height):
			for x in range(width):
				if tile_data[y][x] == '1':
					pos = glm.vec2(unit_width * x, unit_height * y)
					size = glm.vec2(unit_width, unit_height)

					obj = GameObject(pos, size, ResourceManager.get_texture("block_solid"), glm.vec3(0.8, 0.8, 0.7))
					obj.is_solid = True
					self.bricks.append(obj)
					print(obj)

				elif tile_data[y][x] >= '2':
					color = glm.vec3(1.0)
					
					if tile_data[y][x] == '2':
						color = glm.vec3(0.2, 0.6, 1.0)

					elif tile_data[y][x] == '3':
						color = glm.vec3(0.0, 0.7, 0.0)

					elif tile_data[y][x] == '4':
						color = glm.vec3(0.8, 0.8, 0.4)

					elif tile_data[y][x] == '5':
						color = glm.vec3(1.0, 0.5, 0.0)

					pos = glm.vec2(unit_width * x, unit_height * y)
					size = glm.vec2(unit_width, unit_height)

					self.bricks.append(GameObject(pos, size, ResourceManager.get_texture("block"), color))

	def draw(self, renderer):
		for tile in self.bricks:
			print("test")
			tile.draw(renderer)
