from PIL import Image, ImageFilter, ImageStat, ImageEnhance
import os.path
from os import path


def main():
    """
        @param: The file contains photos

        @return: Check the path file whether it exists or not
    """
    im = Image.open("./img/Brightness/camera.jpg")

    # Check the path file whether it exists or not
    print ("file exist:"+str(path.exists('./img/Brightness/camera.jpg')))
    print ("File exists:" + str(path.exists('./img/Brightness/camera.pdf')))
    print ("Directory exists:" + str(path.exists('./img/Brightness/camera.jpg')))

    # To check if the path points to a directory or not
    print ("Is it Directory?" + str(path.isdir('./img/Brightness/camera.jpg')))
    print ("Is it Directory?" + str(path.isdir('./img')))

    enhancer = ImageEnhance.Brightness(im)
    enhanced_im = enhancer.enhance(1.8)
    enhanced_im.save("./img/Brightness/camera.jpg")


class _Enhance:
    """      
        @param: A floating point value controlling the enhancement.
                Factor 1.0 always returns a copy of the original image.
                Lower factors mean less color (brightness, contrast,
                etc), and higher values more.
                There are no restrictions on this value.

        @returns: an enhanced image.
    """
    def enhance(self, factor):
        return Image.blend(self.degenerate, self.image, factor)


class Color(_Enhance):
    """
        @param: This class can be used to adjust the colour balance of an image.
                An enhancement factor of 0.0 gives a black and white image.
                A factor of 1.0 gives the original image.

        @return: Adjust image color balance.
    """
    def __init__(self, image):
        self.image = image
        self.intermediate_mode = 'L'
        if 'A' in image.getbands():
            self.intermediate_mode = 'LA'

        self.degenerate = image.convert(self.intermediate_mode).convert(image.mode)


class Contrast(_Enhance):
    """
        @param: This class can be used to control the contrast of an image.
                An enhancement factor of 0.0 gives a solid grey image.
                A factor of 1.0 gives the original image.
        
        @return: Adjust image contrast.
    """
    def __init__(self, image):
        self.image = image
        mean = int(ImageStat.Stat(image.convert("L")).mean[0] + 0.5)
        self.degenerate = Image.new("L", image.size, mean).convert(image.mode)

        if 'A' in image.getbands():
            self.degenerate.putalpha(image.split()[-1])


class Brightness(_Enhance):
    """
        @param: This class can be used to control the brighntess of an image.
                An enhancement factor of 0.0 gives a black image.
                A factor of 1.0 gives the original image.

        @return: Adjust image brightness.
    """
    def __init__(self, image):
        self.image = image
        self.degenerate = Image.new(image.mode, image.size, 0)

        if 'A' in image.getbands():
            self.degenerate.putalpha(image.split()[-1])
        print(self.image)


class Sharpness(_Enhance):
    """
        @param: This class can be used to adjust the sharpness of an image.
        An enhancement factor of 0.0 gives a blurred image,
        a factor of 1.0 gives the original image, and a factor of 2.0 gives a sharpened image.

        @return: Adjust image sharpness.
    """
    def __init__(self, image):
        self.image = image
        self.degenerate = image.filter(ImageFilter.SMOOTH)

        if 'A' in image.getbands():
            self.degenerate.putalpha(image.split()[-1])

# call class
img = Image.open("./img/Brightness/camera.jpg")
img = Color(img)
img = Contrast(img.image)
img = Brightness(img.image)
img = Sharpness(img.image)
img.image.show()


if __name__== "__main__":
   main()