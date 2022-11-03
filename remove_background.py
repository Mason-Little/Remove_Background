import os
import random
import rembg
import cv2
from PIL import Image, ImageStat
from multiprocessing import Pool
from tqdm import tqdm


def process(input_path, count, interior_exterior):
    if interior_exterior == 'exterior':
        output_path = f'Data\\Output\\exterior\\output{count}.png'
    else:
        output_path = f'Data\\Output\\interior\\output{count}.png'
    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            o.write(rembg.bg.remove(i.read()))

    im = cv2.imread(output_path, cv2.IMREAD_UNCHANGED)
    x, y, w, h = cv2.boundingRect(im[..., 3])
    im2 = im[y:y + h, x:x + w, :]
    cv2.imwrite(output_path, im2)

    image = Image.open(output_path)
    new_image = Image.new("RGBA", image.size, "WHITE")  # Create a white rgba background
    new_image.paste(image, (0, 0), image)  # Paste the image on the background. Go to the links given below for details.
    new_image.convert('RGB').save(output_path, "JPEG")  # Save as JPEG

    im = Image.open(output_path).convert('L')
    stat = ImageStat.Stat(im)
    return stat

def interior():
    root = r'Data\\Input\\interior'
    interior_exterior = root.split('\\')[-1]
    count = 0
    for input in tqdm([file for file in os.listdir(root)], total=len(os.listdir(root))):
        try:
            count += 1
            input = os.path.join(root, input)
            process(input, count, interior_exterior)
        except:
            pass


def exterior():
    root = r'..\\Data\\Input\\exterior'
    interior_exterior = root.split('\\')[-1]
    count = 0
    for input in tqdm([file for file in os.listdir(root)], total=len(os.listdir(root))):
        try:
            count += 1
            input = os.path.join(root, input)

            process(input, count, interior_exterior)
        except:
            pass


def main():
    interior()
    exterior()

if __name__ == '__main__':
    main()
