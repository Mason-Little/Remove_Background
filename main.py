import os
import random
import rembg
import cv2
from PIL import Image, ImageStat
from multiprocessing import Pool
from tqdm import tqdm


def process_inside(input_path):
    root = r'D:\Data\inside_outside_s\non-vehicles'
    input_path = os.path.join(root, input_path)
    output_path = fr'data\outside\output{random.randint(0, 19023847192384)}.png'
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

def process_outside(input_path):
    root = r'D:\Data\inside_outside_s\non-vehicles'
    input_path = os.path.join(root, input_path)
    output_path = fr'data\outside\output{random.randint(0, 19023847192384)}.png'
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

def inside():
    file_path = r"D:\Data\Inside_Outside_s\non-vehicles"
    # with Pool() as p:
    #     inside = p.map(process_inside, [file for file in os.listdir(file_path)])

    for input in [file for file in os.listdir(file_path)]:
        process_inside(input)


def outside():
    file_path = r"D:\Data\Inside_Outside_s\vehicles"
    with Pool() as p:
        outside = p.map(process_outside, [os.path.join(file_path, file) for file in os.listdir(file_path)])

    return outside


def main():
    inside()

if __name__ == '__main__':
    main()


