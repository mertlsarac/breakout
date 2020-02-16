import glm
from texture import *

class GameObject:
	def __init__(self, position, size, sprite, color = glm.vec3(1.0)):
		self.position = position
		self.size = size
		self.sprite = sprite
		self.color = color
		self.velocity = 0.0
		self.rotation = 0.0
		self.is_solid = False
		self.destroyed = False

	def draw(self, renderer):
		renderer.draw_sprite(texture=self.sprite, position=self.position, size=self.size, rotate=0.0, color=self.color)