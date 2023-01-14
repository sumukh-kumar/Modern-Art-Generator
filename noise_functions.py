import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
from random import *


def pnoise(color):
    noise1 = PerlinNoise(octaves=randint(1,10))
    noise2 = PerlinNoise(octaves=randint(1,10))
    noise3 = PerlinNoise(octaves=randint(1,10))
    noise4 = PerlinNoise(octaves=randint(1,10))

    xpix, ypix = 100, 100
    pic = []
    for i in range(xpix):
        row = []
        for j in range(ypix):
            noise_val =  noise1([i/xpix, j/ypix])
            noise_val += 0.5 * noise2([i/xpix, j/ypix])
            noise_val += 0.25* noise3([i/xpix, j/ypix])
            noise_val += 0.125 * noise4([i/xpix, j/ypix])

            row.append(noise_val)
        pic.append(row)

    plt.imshow(pic, cmap=color)
    plt.show()
