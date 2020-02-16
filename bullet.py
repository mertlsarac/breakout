import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version

p.setGravity(0,0,-1)

cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])

cuid = p.createCollisionShape(p.GEOM_BOX, halfExtents = [1, 1, 1])
mass= 1 #static box

body = p.createMultiBody(mass,cuid)

for i in range(100000):
	p.stepSimulation()

print("asd")
position = p.getBasePositionAndOrientation(body)
print(position)
print("asd")
p.disconnect()
