import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class OrbitaKepler:
    def __init__(self, a, e, M):
        self.a = a  # Semieje mayor
        self.e = e  # Excentricidad
        self.M = M  # Masa del cuerpo central
        self.G = 6.67430e-11  # Constante gravitacional
        self.mu = self.G * self.M  # Parámetro gravitacional
        self.T = 2 * np.pi * np.sqrt(self.a**3 / self.mu)  # Período orbital

    def calcular_radio(self, theta):
        return (self.a * (1 - self.e**2)) / (1 + self.e * np.cos(theta))

    def obtener_coordenadas(self, num_points=1000):
        theta = np.linspace(0, 2 * np.pi, num_points)
        r = self.calcular_radio(theta)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        return x, y

def graficar_orbitas(orbitas, num_points=1000):
    fig, ax = plt.subplots(figsize=(8, 8))
    bodies = []

    for orbita in orbitas:
        x, y = orbita.obtener_coordenadas(num_points)
        ax.plot(x, y, label=f'Órbita con a={orbita.a}, e={orbita.e}, T={orbita.T:.2e} s')
        body, = ax.plot([], [], 'ro')  # El cuerpo en la órbita
        bodies.append(body)

    plt.scatter([0], [0], color='orange', label='Cuerpo central')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Representación de órbitas usando las leyes de Kepler')
    plt.legend(loc = "upper left")
    plt.grid(True)
    ax.set_aspect('equal', adjustable='box')

    def init():
        for body in bodies:
            body.set_data([], [])
        return bodies

    def animate(i):
        for j, orbita in enumerate(orbitas):
            theta = 2 * np.pi * (i / num_points) * (1 / (orbita.T / orbitas[0].T))
            r = orbita.calcular_radio(theta)
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            bodies[j].set_data(x, y)
        return bodies

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_points, interval=20, blit=True)
    plt.show()

# Solicitar datos al usuario para múltiples órbitas
num_orbitas = int(input("Introduce el número de órbitas: "))
orbitas = []
M = float(input("Introduce la masa del cuerpo central (en kg): "))

for i in range(num_orbitas):
    print(f"\nDatos para la órbita {i+1}:")
    a = float(input("Introduce el semieje mayor (en metros): "))
    e = float(input("Introduce la excentricidad: "))
    orbitas.append(OrbitaKepler(a=a, e=e, M=M))

graficar_orbitas(orbitas)


