from enum import Enum
from resourceManager import *
import glm
from spriteRenderer import *
from GameLevel import *
from ballObject import *

class State:
	GAME_ACTIVE, GAME_MENU, GAME_WIN = range(0, 3)

class Game:
	def __init__(self, width, height):
		self.width = width;
		self.height = height

		self.state = State.GAME_ACTIVE
		self.keys = [GL_FALSE for i in range(1024)]

		self.levels = []
 
	def init(self):
		ResourceManager.load_shader("vertex.glsl", "fragment.glsl", "sprite")

		projection = glm.ortho(0.0, self.width, self.height, 0.0, -1.0, 1.0)

		ResourceManager.get_shader("sprite").use().set_integer("image", 0)
		ResourceManager.get_shader("sprite").set_matrix_4f("projection", projection)

		self.Renderer = SpriteRenderer(ResourceManager.get_shader("sprite"))

		#load textures
		ResourceManager.load_texture("background.jpg", GL_FALSE, "background")
		ResourceManager.load_texture("awesomeface.png", GL_FALSE, "face")
		ResourceManager.load_texture("block.png", GL_FALSE, "block")
		ResourceManager.load_texture("block_solid.png", GL_FALSE, "block_solid")
		ResourceManager.load_texture("paddle.png", GL_FALSE, "paddle")

		level_1 = GameLevel()
		level_1.load("level_1", self.width, self.height * 0.5)

		self.levels.append(level_1)

		#player
		self.PLAYER_SIZE = glm.vec2(100, 20)
		self.PLAYER_VELOCITY = 500.0

		self.player_pos = glm.vec2(float(self.width / 2 - self.PLAYER_SIZE.x / 2), float(self.height - self.PLAYER_SIZE.y / 2))

		self.player = GameObject(self.player_pos, self.PLAYER_SIZE, ResourceManager.get_texture("paddle"))

		#ball
		INITIAL_BALL_VELOCITY = glm.vec2(100.0, -350.0)
		BALL_RADIUS = 12.5

		ballpos = self.player_pos + glm.vec2(self.PLAYER_SIZE.x / 2 - BALL_RADIUS, -BALL_RADIUS * 2)
		self.ball = BallObject(ballpos, None, ResourceManager.get_texture("face"), glm.vec3(1.0), INITIAL_BALL_VELOCITY, BALL_RADIUS, True)
 		
	def process_input(self, dt): 
		if self.state == State.GAME_ACTIVE:
			velocity = self.PLAYER_VELOCITY * dt

			if self.keys[glfw.KEY_A] == GL_TRUE:
				if self.player.position.x >= 0:
					self.player.position.x -= velocity

					if self.ball.stuck:
						self.ball.position.x -= velocity


			if self.keys[glfw.KEY_D]:
				if self.player.position.x <= self.width - self.player.size.x:
					self.player.position.x += velocity
					if self.ball.stuck:
						self.ball.position.x += velocity

			if self.keys[glfw.KEY_SPACE]:
				self.ball.stuck = False

	def update(self, dt):
		self.ball.move(dt, self.width)

	def render(self):
		if self.state == State.GAME_ACTIVE:
			self.Renderer.draw_sprite(texture=ResourceManager.get_texture("background"), position=glm.vec2(0.0, 0.0), size=glm.vec2(self.width, self.height), rotate=0.0)
			self.levels[0].draw(self.Renderer)
			self.player.draw(self.Renderer)
			self.ball.draw(self.Renderer)