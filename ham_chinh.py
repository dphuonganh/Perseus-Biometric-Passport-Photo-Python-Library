import os.path, face_recognition
from os import path
from PIL import Image

def main():
    """
        @param: The file contains photos

        @return: Check the path file whether it exists or not
    """
    im = Image.open("./img/Brightness/camera.jpg")

def check_file_exist(path):
    path = input()
    try:
        with open(path, 'rb') as image_file:
            image = face_recognition.load_image_file(image_file)
            return image
    except IOError:
        print("File not valid")

if __name__== "__main__":
   main()
   check_file_exist(path)


