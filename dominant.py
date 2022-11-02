import os
from colorthief import ColorThief
import matplotlib.pyplot as plt
from tqdm import tqdm

root = r'D:\\A.I\\Remove_Background\\data\\interior'
image_list = os.listdir(root)
count = 0
for image in tqdm(image_list, total=len(image_list)):
    try:
        count += 1
        color_thief = ColorThief(os.path.join(root, image))
        palette = color_thief.get_palette(color_count=2)
        plt.imshow([[palette[i] for i in range(2)]])
        plt.savefig(fr"data\Inside_Dominant\inside {count}.png")
        # plt.show()
    except:
        pass

root = r'D:\A.I\\Remove_Background\\data\\exterior'
image_list = os.listdir(root)
count = 0

for image in tqdm(image_list, total=len(image_list)):
    try:
        count += 1
        color_thief = ColorThief(os.path.join(root, image))
        palette = color_thief.get_palette(color_count=2)
        plt.imshow([[palette[i] for i in range(2)]])
        plt.savefig(fr"data\Outside_Dominant\outside {count}.png")
        # plt.show()
    except:
        pass
