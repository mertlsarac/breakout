import glfw
from OpenGL.GL import *
from game import *
from resourceManager import *

def key_callback(window, key, scancode, action, mode):
	if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
		glfw.set_window_should_close(window, GL_TRUE)

	if key >= 0 and key < 1024:
		if action == glfw.PRESS:
			breakout.keys[key] = GL_TRUE
		elif action == glfw.RELEASE:
			breakout.keys[key] = GL_FALSE

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

breakout = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

glfw.init()
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
glfw.window_hint(glfw.RESIZABLE, GL_FALSE)

window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Breakout", None, None)

glfw.make_context_current(window)

glfw.set_key_callback(window, key_callback)

glViewport(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

glEnable(GL_CULL_FACE)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

breakout.init()

deltaTime = 0.0
lastFrame = 0.0

breakout.State = State.GAME_ACTIVE

while not glfw.window_should_close(window):
	currentFrame = glfw.get_time()
	deltaTime = currentFrame - lastFrame
	lastFrame = currentFrame

	glfw.poll_events()

	breakout.process_input(deltaTime)

	breakout.update(deltaTime)

	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClear(GL_COLOR_BUFFER_BIT)

	breakout.render()

	glfw.swap_buffers(window)

ResourceManager.clear()

glfw.terminate()
