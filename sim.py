import numbpy as np

gravity = np.array([0,-10]) 
width = 10, height = 10
changeInTime = 1

class Particle:
  def initialise(self, mass = 1 radius = 1, position, velocity):
    self.position = np.array(position, dtype = float)
    self.velocity = np.array(velocity, dtype=float)
    self.radius = radius
    self.mass = mass
  
  def update(self):
    self.velocity += gravity * changeInTime
    self.position += self.velocity * changeInTime

  def wallCollision(self):
    
