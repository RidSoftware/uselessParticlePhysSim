import numpy as np
import random

import matplotlib.pyplot as plt
import matplotlib.animation as animation

gravity = np.array([0,-10]) 
width, height = 10, 10
changeInTime = 1

class Particle:
  def initialise(self, mass = 1, radius = 1, position, velocity):
    self.position = np.array(position, dtype = float)
    self.velocity = np.array(velocity, dtype=float)
    self.radius = radius
    self.mass = mass
  
  def update(self):
    self.velocity += gravity * changeInTime
    self.position += self.velocity * changeInTime
    self.wallCollision()

  def wallCollision(self):
    for i in range(2):
      if self.position[i] - self.radius < 0:
        self.position[i] = self.radius
        self.velocity[i] *= -0.5
      else if self.position[i] + self.radius > (width if i == 0 else height):
        self.position[i] = (width if i == 0 else height) - self.radius
        self.velocity[i] *= -0.5

particles = [
    Particle(position=[random.uniform(1, 9), random.uniform(5, 9)],
             velocity=[random.uniform(-1, 1), random.uniform(-1, 1)])
    for _ in range(10)
]

fig, ax = plt.subplots()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
scat = ax.scatter([p.position[0] for p in particles],
                 [p.position[1] for p in particles], s=100)

def animate(frame):
    for p in particles:
        p.update()
    scat.set_offsets([p.position for p in particles])
    return scat,

ani = animation.FuncAnimation(fig, animate, frames=200, interval=20, blit=True)
plt.show()
