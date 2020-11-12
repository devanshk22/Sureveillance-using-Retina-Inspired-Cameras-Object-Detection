import matplotlib.patches as patches
import numpy as np


def draw_boxes(frame, x_coords, y_coords):
    if not x_coords or not y_coords:
        return 0
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

    rectangles = []
    label_coords = []

    if len(x_coords) == len(y_coords):
        for i in range(0, (len(x_coords)-1), 2):
            for j in range(0, len(y_coords)-1, 2):
                x_min = x_coords[i]
                x_max = x_coords[i+1]
                y_min = y_coords[j]
                y_max = y_coords[j+1]
                width = (x_max - x_min)
                height = (y_max - y_min)
                num_pixels = np.sum(frame[y_min:y_max+1, x_min:x_max+1])
                if num_pixels < 5:
                    continue
                else:
                    rect = patches.Rectangle((x_min, y_min), width, height, linewidth=1, edgecolor='r',
                                             facecolor='none')
                    rectangles.append(rect)
                    x_label = x_max - 10
                    y_label = y_min - 2
                    label_coords.append((x_label, y_label))
    else:
        if len(x_coords) > len(y_coords):
            for i in range(0, len(y_coords)-1, 2):
                y_min = y_coords[i]
                y_max = y_coords[i+1]
                for j in range(0, len(x_coords)-1, 2):
                    x_min = x_coords[j]
                    x_max = x_coords[j+1]
                    width = (x_max - x_min)
                    height = (y_max - y_min)
                    rect = patches.Rectangle((x_min, y_min), width, height, linewidth=1, edgecolor='r',
                                             facecolor='none')
                    rectangles.append(rect)
                    x_label = x_max
                    y_label = y_min + 1
                    label_coords.append((x_label, y_label))
        else:
            for i in range(0, len(x_coords)-1, 2):
                x_min = y_coords[i]
                x_max = y_coords[i+1]
                for j in range(0, len(y_coords)-1, 2):
                    y_min = x_coords[j]
                    y_max = x_coords[j+1]
                    width = (x_max - x_min)
                    height = (y_max - y_min)
                    rect = patches.Rectangle((x_min, y_min), width, height, linewidth=1, edgecolor='r',
                                             facecolor='none')
                    rectangles.append(rect)
                    x_label = x_max
                    y_label = y_min + 1
                    label_coords.append((x_label, y_label))

    if rectangles:
        return rectangles, label_coords
    else:
        return 0
