import numpy as np
import matplotlib.pyplot as plt
from noise import pnoise2

def generate_terrain(size, scale=100):
    terrain = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            terrain[i][j] = pnoise2(i/scale, j/scale, octaves=6)
    return terrain

def plot_terrain(terrain):
    plt.imshow(terrain, cmap="terrain")
    plt.colorbar()
    plt.title("Procedural Terrain Generation using Perlin Noise")
    plt.show()

terrain = generate_terrain(100)
plot_terrain(terrain)
