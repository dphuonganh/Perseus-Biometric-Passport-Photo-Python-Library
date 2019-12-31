from PIL import Image
import argparse
import face_recognition


def check_file_exist(path):
    try:
        with open(path, 'rb') as image_file:
            image = face_recognition.load_image_file(image_file)
            return image
    except OSError:
        pass


def background(image):
    # image = Image.open("./img/Brightness/gray.jpg")
    Exist= check_file_exist(image)
    # Convert the image te RGBA if it is a .gif for example
    imge = Image.fromarray(Exist) # open ('./img/Brightness/gray.jpeg')
    img = imge.convert("RGBA")

    pixdata = img.load()
    background = pixdata[0, 0]
    print(background)
    return background


def result_background(image):
    pixel = background(image)
    if pixel[0] in range(167,208) and pixel[1] in range(167,208) and pixel[2] in range(167,208):
        print("Gray background")
        return True
    else:
        print("Not Gray background")
        return False


parser = argparse.ArgumentParser(
        description='Detects faces in the given image.')

parser.add_argument(
    "image", 
    help='the image you\'d like to detect faces in.')

parser.add_argument(
    'mode', help='Set to call function need to do')

args = parser.parse_args()


if args.mode == 'background':
    result_background(args.image)


# RUNN python check_background.py ./img/Brightness/camera.jpg background