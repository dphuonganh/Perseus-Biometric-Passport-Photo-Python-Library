from PIL import Image, ImageFilter, ImageStat, ImageEnhance
import face_recognition, argparse
from os import path
from math import sqrt

def check_file_exist(path):
    try:
        with open(path, 'rb') as image_file:
            image = face_recognition.load_image_file(image_file)
            return image
    except OSError:
        pass


def brightness(image):
    # image = Image.open("./img/Brightness/camera.jpg")
    Exist = check_file_exist(image) # Image exist
    # Convert the image te RGB if it is a .gif for example
    image = Image.fromarray(Exist)
    imag = image.convert ('RGB')
    # coordinates of the pixel
    X,Y = 0,0
    # Get RGB
    pixelRGB = imag.getpixel((X,Y))
    R,G,B = pixelRGB 
    brightness = sum([R,G,B])/3 # 0 is dark (black) and 255 is bright (white)
    print(brightness)
    return brightness


def brightness_detection(image):
    Brightness = brightness(image)
    threshold = 125.0
    if Brightness < threshold:
        print("{}: {:.2f}".format('Too dark brightness', Brightness)) # lay so thap phan
        return False
    else:
        print("{}: {:.2f}".format('Brightness is right', Brightness)) # lay so thap phan
        return True


def result_brightness(image):
    if brightness_detection(image) == True:
        return True
    else:
        return False


parser = argparse.ArgumentParser(
        description='Detects faces in the given image.')

parser.add_argument(
    "image", 
    help='the image you\'d like to detect faces in.')

parser.add_argument(
    'mode', help='Set to call function need to do')

args = parser.parse_args()


if args.mode == 'brightness':
    result_brightness(args.image)


# RUNN python test.py ./img/Brightness/camera.jpg brightness