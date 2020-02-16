import glm
import numpy
from OpenGL.GL import *
class SpriteRenderer:
	def __init__(self, shader):
		self.shader = shader
		self.__init_render_data()

	def draw_sprite(self, texture, position, size=glm.vec2(10, 10), rotate=0.0, color=glm.vec3(1.0)):
		self.shader.use()

		model = glm.mat4()
		model = glm.translate(model, glm.vec3(position, 0.0))

		model = glm.translate(model, glm.vec3(0.5 * size.x, 0.5 * size.y, 0.0))
		model = glm.rotate(model, rotate, glm.vec3(0.0, 0.0, 1.0))
		model = glm.translate(model, glm.vec3(-0.5 * size.x, -0.5 * size.y, 0.0))

		model = glm.scale(model, glm.vec3(size, 1.0))

		self.shader.set_matrix_4f("model", model)

		self.shader.set_vector_3f("spriteColor", color)

		glActiveTexture(GL_TEXTURE0)
		texture.bind()

		glBindVertexArray(self.quadVAO)
		glDrawArrays(GL_TRIANGLES, 0, 6)
		glBindVertexArray(0)

	def __init_render_data(self):
		#poss	tex

		vertices = [
			0.0, 1.0,	0.0, 1.0,
			1.0, 0.0,	1.0, 0.0,
			0.0, 0.0,	0.0, 0.0,

			0.0, 1.0,	0.0, 1.0,
			1.0, 1.0,	1.0, 1.0,
			1.0, 0.0,	1.0, 0.0]

		vertices = numpy.array(vertices, dtype=numpy.float32)

		self.quadVAO = glGenVertexArrays(1)
		VBO = glGenBuffers(1)

		glBindBuffer(GL_ARRAY_BUFFER, VBO)
		glBufferData(GL_ARRAY_BUFFER, len(vertices) * numpy.dtype(numpy.float32).itemsize, vertices, GL_STATIC_DRAW)

		glBindVertexArray(self.quadVAO)
		glEnableVertexAttribArray(0)
		glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, numpy.dtype(numpy.float32).itemsize * 4, None)
		glBindBuffer(GL_ARRAY_BUFFER, 0)
		glBindVertexArray(0)
