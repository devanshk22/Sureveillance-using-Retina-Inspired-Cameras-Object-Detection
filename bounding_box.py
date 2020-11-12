import numpy as np
# import matplotlib.pyplot as plt


def bounding_box(x_hist, y_hist, x_threshold=1, y_threshold=1):
    x_coords = []
    y_coords = []
    started = False
    x_count = 0
    y_count = 0
    for i in range(1, len(x_hist)-1):
        if (x_hist[i] > x_threshold) and (x_hist[i-1] > x_threshold) and (not started):
            started = True
            x_count += 1
            x_coords.append(i)
        elif started and (x_hist[i + 1] >= x_threshold):
            continue
        elif started and (x_hist[i + 1] < x_threshold):
            started = False
            x_coords.append(i)
        else:
            continue

    started = False
    for j in range(1, len(y_hist)-1):
        if (y_hist[j] > y_threshold) and (y_hist[j-1] > y_threshold) and (not started):
            started = True
            y_count += 1
            y_coords.append(j)
        elif started and (y_hist[j + 1] >= y_threshold):
            continue
        elif started and (y_hist[j + 1] < y_threshold):
            started = False
            y_coords.append(j)
        else:
            continue

    return x_coords, y_coords


def form_x_hist(frame):
    y_len, x_len = frame.shape
    x_hist = np.zeros((1, x_len), dtype='uint8')
    for i in range(x_len):
        hist_val = 0
        for j in range(y_len):
            hist_val += frame[j, i]
        x_hist[0, i] = hist_val
    # add parameter ax to the function and uncomment the following line to visualise histograms
    # ax.bar(x=range(x_len), height=x_hist[0])
    return x_hist[0]


def form_y_hist(frame):
    y_len, x_len = frame.shape
    y_hist = np.zeros((1, y_len), dtype='uint8')
    for i in range(y_len):
        hist_val = 0
        for j in range(x_len):
            hist_val += frame[i, j]
        y_hist[0, i] = hist_val
    # add parameter ax to the function and uncomment the following lines to visualise histograms
    # ax.invert_yaxis()
    # ax.barh(y=range(y_len), width=y_hist[0])
    return y_hist[0]
