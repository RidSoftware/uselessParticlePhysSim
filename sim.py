import numbpy as np

gravity = np.array([0,-10]) 
width = 10, height = 10
changeInTime = 1

class Particle:
  def initiallize(self, mass = 1 radius = 1, position, velocity):
    self.position = np.array(position, dtype = float)
