from PIL import Image, ImageFilter, ImageStat


class _Enhance:

    def enhance(self, factor):
        return Image.blend(self.degenerate, self.image, factor)


class Color(_Enhance):
    def __init__(self, image):
        self.image = image
        self.intermediate_mode = 'L'
        if 'A' in image.getbands():
            self.intermediate_mode = 'LA'

        self.degenerate = image.convert(self.intermediate_mode).convert(image.mode)

class Contrast(_Enhance):
    def __init__(self, image):
        self.image = image
        mean = int(ImageStat.Stat(image.convert("L")).mean[0] + 0.5)
        self.degenerate = Image.new("L", image.size, mean).convert(image.mode)

        if 'A' in image.getbands():
            self.degenerate.putalpha(image.split()[-1])


class Brightness(_Enhance):
    def __init__(self, image):
        self.image = image
        self.degenerate = Image.new(image.mode, image.size, 0)

        if 'A' in image.getbands():
            self.degenerate.putalpha(image.split()[-1])
        print(self.image)

class Sharpness(_Enhance):
    def __init__(self, image):
        self.image = image
        self.degenerate = image.filter(ImageFilter.SMOOTH)

        if 'A' in image.getbands():
            self.degenerate.putalpha(image.split()[-1])


    file1 = './known/massu.jpg'
image = Brightness(file1)
print(image)