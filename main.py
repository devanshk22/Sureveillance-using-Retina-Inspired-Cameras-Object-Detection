from matplotlib import pyplot as plt
import form_frame
import bounding_box
import compression
from skimage.filters import median
from skimage.morphology import disk
import draw_boxes
import pandas as pd

filename = 'data/night_100m_50.bin'
frame_time = 66000  # Assume that each frame corresponds to 66 microseconds
start_time = 3003957837
# 3003957837 night 100m 50
frames = pd.read_csv('timestamp_250pixel.csv')
num_frames = frames.shape[0]
count = 0
# frame, td = form_frame.form_frame(filename, start_time, frame_time)
# median_filtered_frame = median(frame, disk(1), mode='constant', cval=0.0)
# fig, axs = plt.subplots(2, 2, figsize=(10, 10))
# x_hist = bounding_box.form_x_hist(median_filtered_frame)
# y_hist = bounding_box.form_y_hist(median_filtered_frame)
# compressed_x_frame, compressed_y_frame = compression.compress_frame(x_hist, y_hist)
# axs[1, 0].set_title('Frame')
# axs[0, 0].set_title('X-Histogram')
# axs[1, 1].set_title('Y-Histogram')
# axs[1, 0].imshow(median_filtered_frame)
# axs[0, 0].bar(x=range(len(x_hist)), height=x_hist)
# axs[1, 1].invert_yaxis()
# axs[1, 1].barh(y=range(len(y_hist)), width=y_hist, color='red')
# axs[0, 1].set_title('Compressed X-histogram')
# axs[0, 1].bar(x=range(len(compressed_x_frame)), height=compressed_x_frame)
#
# plt.show()

for i in range(num_frames):
    curr_row = frames.iloc[i]
    if curr_row['object presence'] == 1:
        count += 1  # frame number
        start_time = curr_row['timestamp start']
        frame, td = form_frame.form_frame(filename, start_time, frame_time)
        median_filtered_frame = median(frame, disk(1), mode='constant', cval=0.0)
        x_hist = bounding_box.form_x_hist(median_filtered_frame)
        y_hist = bounding_box.form_y_hist(median_filtered_frame)
        compressed_x_frame, compressed_y_frame = compression.compress_frame(x_hist, y_hist)

        x_coords, y_coords = bounding_box.bounding_box(compressed_x_frame, compressed_y_frame)

        try:
            boxes, label_coords = draw_boxes.draw_boxes(median_filtered_frame, x_coords, y_coords)
            num_boxes = len(boxes)
        except TypeError:
            continue
        fig, axs = plt.subplots(1, 1, figsize=(10, 10))
        plt.imshow(median_filtered_frame)
        for j in range(num_boxes):
            axs.add_patch(boxes[j])
            x, y = label_coords[j]
            plt.text(x, y, s='Object'+str(j+1), color='red')

        plt.axis('off')
        num_str = str(count)
        num_str = num_str.zfill(3)
        file_path = 'final_img2/'+num_str+'.jpg'
        plt.savefig(file_path, bbox_inches='tight')
        print('Frames left: '+str(num_frames-i))

# The code below can be used to plot the histograms and/or the individual frames

# fig, axs = plt.subplots(3, 2, figsize=(10, 10))
# fig.tight_layout(pad=1.5)
# axs[0, 0].set_title('X Histogram')
# axs[1, 0].set_title('Frame')
# axs[1, 1].set_title('Y Histogram')
# axs[0, 1].set_title('Box coordinates')
# axs[2, 0].set_title('Compressed X histogram')
# axs[2, 1].set_title('Compressed Y histogram')
# axs[0, 0].bar(x=range(len(x_hist)), height=x_hist)
# axs[1, 1].invert_yaxis()
# axs[1, 1].barh(y=range(len(y_hist)), width=y_hist, color='red')
# # axs[0, 1].invert_yaxis()
# # axs[0, 1].barh(y=range(len(compressed_y_frame)), width=compressed_y_frame)
# axs[2, 0].bar(x=range(len(compressed_x_frame)), height=compressed_x_frame)
# axs[2, 1].invert_yaxis()
# axs[2, 1].barh(y=range(len(compressed_y_frame)), width=compressed_y_frame, color='red')
# plt.show()
