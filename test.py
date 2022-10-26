import os
from colorthief import ColorThief
import matplotlib.pyplot as plt
from tqdm import tqdm

root = r'D:\Data\testing_x'
image_list = os.listdir(root)

for image in tqdm(image_list, total=len(image_list)):
    color_thief = ColorThief(os.path.join(root, image))
    palette = color_thief.get_palette(color_count=2)
    plt.imshow([[palette[i] for i in range(2)]])
    plt.show()
    # print(palette)
