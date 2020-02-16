from gameObject import *
class BallObject(GameObject):
	def __init__(self, position, size, sprite, color, velocity, radius, stuck):
		self.position = position
		self.size = glm.vec2(radius * 2, radius * 2)
		self.sprite = sprite
		self.color = color 

		self.velocity = velocity
		self.radius = radius
		self.stuck = stuck

	def move(self, dt, window_width):
		if not self.stuck:
			self.position += self.velocity * dt

			if self.position.x <= 0.0:
				self.velocity.x = -self.velocity.x

			elif self.position.x + self.size.x >= window_width:
				self.velocity.x = -self.velocity.x
				self.position.x = window_width - self.size.x

			if self.position.y <= 0.0:
				self.velocity.y = -self.velocity.y
				self.position.y = 0.0

		return self.position

	def reset(self, position, velocity):
		self.position = position
		self.velocity = velocity
		self.stuck = True