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


def decompress(x_hist, y_hist, x_factor=6, y_factor=3):
    x_decompressed = []
    y_decompressed = []
    for i in x_hist:
        decompressed = [0]*x_factor
        if i != 0:
            mid = math.ceil(x_factor/2)
            decompressed[mid] = 1
        x_decompressed.extend(decompressed)

    for j in y_hist:
        decompressed = [0]*y_factor
        if j != 0:
            mid = math.ceil(y_factor/2)
            decompressed[mid] = 1
        y_decompressed.extend(decompressed)

    return x_decompressed, y_decompressed
