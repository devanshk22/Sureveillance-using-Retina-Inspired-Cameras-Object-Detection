import os
import sys
import video_data_extraction
import pandas as pd
import numpy as np


def form_frame(file_name, start_time, frame_time=66000):
    frame = np.zeros((180, 240), dtype='uint8')  # Initializing frame as all zeros
    filepath = os.path.join(sys.path[0], file_name)
    td = video_data_extraction.read_bin_linux(filepath)

    pixel_data = pd.DataFrame(td)  # Saving the pixel data as a Pandas DataFrame
    num_points = pixel_data.shape[0]  # Number of data points
    pixel_data.sort_values(by='ts', axis=0, ascending=True, inplace=True)  # Sorting the data frame in ascending order
    # by time
    i = 0
    frame_not_ended = True  # boolean variable to check when we have exceeded 66 us so that we can stop forming the
    # frame

    first_row = pixel_data.iloc[0]
    init_time = first_row['ts']
    if init_time > start_time + frame_time:
        print("Error: Frame times start at "+str(init_time))
        return 0

    while i < num_points:
        start = pixel_data.iloc[i]  # Current row as an object

        # Extracting individual values of time
        curr_time = start['ts']
        if curr_time < start_time:
            i += 1
            continue
        else:
            j = 0
            while frame_not_ended:
                row = pixel_data.iloc[i + j]
                t = row['ts']
                if t > curr_time + frame_time:
                    frame_not_ended = False
                else:
                    if frame[row['y'], row['x']] == 0:
                        frame[row['y'], row['x']] = 1
                j += 1
            break
    return frame, td
