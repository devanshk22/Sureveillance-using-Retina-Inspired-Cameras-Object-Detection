import math


def compress_frame(x_hist, y_hist, x_factor=6, y_factor=3):
    x_compressed = []
    i = 0
    while i < len(x_hist):
        val = 0
        for j in range(i, i+x_factor):
            val += x_hist[j]
        x_compressed.append(val)
        i += x_factor

    y_compressed = []
    j = 0
    while j < len(y_hist):
        val = 0
        for k in range(j, j+y_factor):
            val += y_hist[j]
        y_compressed.append(val)
        j += y_factor

    return x_compressed, y_compressed


def decompress(x_coords, y_coords,  x_factor=6, y_factor=3):
    for i in range(len(x_coords)):
        if i % 2 == 0:
            x_coords[i] -= 1
        else:
            x_coords[i] += 1
    for i in range(len(y_coords)):
        if i % 2 == 0:
            y_coords[i] -= 1
        else:
            y_coords[i] += 1

    x_coords = [x * 6 for x in x_coords]  # Scale values back up
    y_coords = [x * 3 for x in y_coords]

    return x_coords, y_coords
