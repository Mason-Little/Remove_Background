import os
from colorthief import ColorThief
import matplotlib.pyplot as plt
from tqdm import tqdm

# Load Data

# Background Kept (Default)
interior = 'Data\\Input\\interior'
exterior = 'Data\\Input\\exterior'

#Background Removed
# interior = '..\\Data\\Output\\interior'
# exterior = '..\\Data\\Output\\exterior'


image_list = os.listdir(interior)
count = 0
for image in tqdm(image_list, total=len(image_list)):
    try:
        count += 1
        color_thief = ColorThief(os.path.join(interior, image))
        palette = color_thief.get_palette(color_count=2)
        plt.imshow([[palette[i] for i in range(2)]])
        plt.savefig(fr"Data\\Output\\Interior_Dominant\\outside{count}.png")
        # plt.show()
    except:
        pass

image_list = os.listdir(exterior)
count = 0

for image in tqdm(image_list, total=len(image_list)):
    try:
        count += 1
        color_thief = ColorThief(os.path.join(exterior, image))
        palette = color_thief.get_palette(color_count=2)
        plt.imshow([[palette[i] for i in range(2)]])
        plt.savefig(f"Data\\Output\\Exterior_Dominant\\outside{count}.png")
        # plt.show()
    except:
        pass
