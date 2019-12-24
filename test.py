from PIL import Image, ImageFilter, ImageStat, ImageEnhance
import os.path, face_recognition, argparse
from os import path


def main():
    im = Image.open("./img/Brightness/camera.jpg")

def check_file_exist(path):
    path = input()
    try:
        with open(path, 'rb') as image_file:
            image = face_recognition.load_image_file(image_file)
            return image
    except IOError:
        print("File not valid")


def enhance(self, factor):
    return Image.blend(self.degenerate, self.image, factor)


def color_detection(self, image):
    self.image = image
    self.intermediate_mode = 'L'
    if 'A' in image.getbands():
        self.intermediate_mode = 'LA'

    self.degenerate = image.convert(self.intermediate_mode).convert(image.mode)


def contrast_detection(self, image):
        self.image = image
        mean = int(ImageStat.Stat(image.convert("L")).mean[0] + 0.5)
        self.degenerate = Image.new("L", image.size, mean).convert(image.mode)
        if 'A' in image.getbands():
            self.degenerate.putalpha(image.split()[-1])


def brightness_detection(self, image):
        self.image = image
        self.degenerate = Image.new(image.mode, image.size, 0)
        if 'A' in image.getbands():
            self.degenerate.putalpha(image.split()[-1])
        print(self.image)


def sharpness_detection(self, image):
        self.image = image
        self.degenerate = image.filter(ImageFilter.SMOOTH)

        if 'A' in image.getbands():
            self.degenerate.putalpha(image.split()[-1])


def result_color(image_file):
    if color_detection(image_file) == True:
        return True
    else:
        return False


def result_brightness(image_file):
    if brightness_detection(image_file) == True:
        return True
    else:
        return False


def result_sharpness(image_file):
    if sharpness_detection(image_file) == True:
        return True
    else:
        return False


def result_contrast(image_file):      
    if contrast_detection(image_file) == True:
        return True
    else:
        return False

parser = argparse.ArgumentParser(
        description='Detects faces in the given image.')

parser.add_argument(
    "image_file", 
    help='the image you\'d like to detect faces in.')

parser.add_argument(
    'mode', help='Set to call function need to do')

args = parser.parse_args()


if args.mode == 'color':
    result_color(args.image_file)

elif args.mode == 'brightness':
    result_brightness(args.image_file)

elif args.mode == 'sharpness':
    result_sharpness(args.image_file)

elif args.mode == "contrast":
    result_contrast(args.image_file)


# RUNN python test.py ./img/Brightness/camera.jpg Brightness