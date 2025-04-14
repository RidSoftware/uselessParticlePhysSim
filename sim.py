import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# Constants
gravity = np.array([0, -9.81])  # Acceleration due to gravity
width, height = 10, 10  # Size of the box
dt = 0.01  # Time step

# Particle class
class Particle:
    def __init__(self, position, velocity, radius=0.1, mass=1.0):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.radius = radius
        self.mass = mass

    def update(self):
        self.velocity += gravity * dt
        self.position += self.velocity * dt
        self.handle_boundary_collision()

    def handle_boundary_collision(self):
        for i in range(2):
            if self.position[i] - self.radius < 0:
                self.position[i] = self.radius
                self.velocity[i] *= -0.8  # lose some energy
            elif self.position[i] + self.radius > (width if i == 0 else height):
                self.position[i] = (width if i == 0 else height) - self.radius
                self.velocity[i] *= -0.8
                
    def handle_particle_collision(self, other):
        delta_pos = self.position - other.position
        dist = np.linalg.norm(delta_pos)
        if dist < self.radius + other.radius and dist > 0:
            # Normalize vector
            normal = delta_pos / dist
            # Relative velocity
            rel_vel = self.velocity - other.velocity
            # Speed along normal
            vel_along_normal = np.dot(rel_vel, normal)
            if vel_along_normal > 0:
                return  # They are moving apart

            # Calculate impulse scalar
            restitution = 0.9
            impulse_scalar = -(1 + restitution) * vel_along_normal
            impulse_scalar /= (1 / self.mass + 1 / other.mass)

            # Apply impulse
            impulse = impulse_scalar * normal
            self.velocity += impulse / self.mass
            other.velocity -= impulse / other.mass

            # Separate overlapping particles
            overlap = self.radius + other.radius - dist
            correction = normal * overlap / 2
            self.position += correction
            other.position -= correction


# Create particles
particles = [
    Particle(position=[random.uniform(1, 9), random.uniform(5, 9)],
             velocity=[random.uniform(-1, 1), random.uniform(-1, 1)])
    for _ in range(10)
]

# Set up visualization
fig, ax = plt.subplots()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
scat = ax.scatter([p.position[0] for p in particles],
                 [p.position[1] for p in particles], s=100)

def animate(frame):
    for i, p in enumerate(particles):
        p.update()
        for j in range(i + 1, len(particles)):
            p.handle_particle_collision(particles[j])
    scat.set_offsets([p.position for p in particles])
    return scat,

ani = animation.FuncAnimation(fig, animate, frames=200, interval=20, blit=True)
ani.save("particle_sim.gif", writer="pillow", fps=30)
print("Animation saved as 'particle_sim.gif'")
