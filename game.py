from enum import Enum
from resourceManager import *
import glm
from spriteRenderer import *
from GameLevel import *
class State:
	GAME_ACTIVE, GAME_MENU, GAME_WIN = range(0, 3)

class Game:
	def __init__(self, width, height):
		self.width = width;
		self.height = height

		self.state = State.GAME_ACTIVE
		self.keys = []

		self.levels = []
 
	def init(self):
		ResourceManager.load_shader("vertex.glsl", "fragment.glsl", "sprite")

		projection = glm.ortho(0.0, self.width, self.height, 0.0, -1.0, 1.0)

		ResourceManager.get_shader("sprite").use().set_integer("image", 0)
		ResourceManager.get_shader("sprite").set_matrix_4f("projection", projection)

		self.Renderer = SpriteRenderer(ResourceManager.get_shader("sprite"))

		#load textures
		ResourceManager.load_texture("background.jpg", GL_FALSE, "background")
		ResourceManager.load_texture("awesomeface.png", GL_TRUE, "face")
		ResourceManager.load_texture("block.png", GL_FALSE, "block")
		ResourceManager.load_texture("block_solid.png", GL_FALSE, "block_solid")
		ResourceManager.load_texture("paddle.png", GL_FALSE, "paddle")

		level_1 = GameLevel()
		level_1.load("level_1", self.width, self.height * 0.5)

		self.levels.append(level_1)

		self.PLAYER_SIZE = glm.vec2(100, 20)
		self.PLAYER_VELOCITY = 500.0

		self.player_pos = glm.vec2(float(self.width / 2 - self.PLAYER_SIZE.x / 2), float(self.height - self.PLAYER_SIZE.y / 2))

		self.player = GameObject(self.player_pos, self.PLAYER_SIZE, ResourceManager.get_texture("paddle"))

 
	def process_input(self, dt): 
		pass

	def update(self, dt):
		pass

	def render(self):
		if self.state == State.GAME_ACTIVE:
			self.Renderer.draw_sprite(texture=ResourceManager.get_texture("background"), position=glm.vec2(0.0, 0.0), size=glm.vec2(self.width, self.height), rotate=0.0)
			self.levels[0].draw(self.Renderer)
			self.player.draw(self.Renderer)