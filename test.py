
# from PIL import Image

# img = Image.open('./img/Brightness/camera.jpg')
# img = img.convert("RGBA")
# datas = img.getdata()

# newData = []
# for item in datas:
#     if item[0] == 255 and item[1] == 255 and item[2] == 255:
#         newData.append((255, 255, 255, 0))
#     else:
#         if item[0] > 150:
#             newData.append((0, 0, 0, 255))
#         else:
#             newData.append(item)
#             print(item)

# img.putdata(newData)
# img.save("./img/Brightness/camera.jpg", "PNG")









# def __init__(self, fd, background_color=None):
#     try:
#         if isinstance(fd, str):
#             self.fd = Image.open(fd)
#         elif isinstance(fd, Path):
#             self.fd = Image.open(fd)
#         elif isinstance(fd, BufferedReader):
#             self.fd = Image.open(fd)
#         elif isinstance(fd, PngImageFile):
#             self.fd = fd
#         if background_color == None:
#             self.background_color = self.find_most_common_color(self.fd)
#         else:
#             self.background_color = background_color
#     except FileNotFoundError:
#         raise FileNotFoundError("FileNotFoundError")

# @staticmethod


# def detect_background_color(self, pixel_list):
#         if self.fd.mode == "RGBA":
#             background_color_list = []
#             for i in range(len(pixel_list)):
#                 for j in range(len(pixel_list[i])):
#                     if pixel_list[i][j][3] == 0:
#                         background_color_list.append(pixel_list[i][j])
#             return background_color_list
#         return find_most_common_color(self.fd)


# def is_background_color(self, pixel, background_color):
#     if isinstance(background_color, set):
#         return pixel in background_color
#     return np.all(pixel == background_color)



# def detect_background_color(pixel_list, image):
#     if image.mode == "RGBA":
#         background_color_list = []
#         for i in range(len(pixel_list)):
#             for j in range(len(pixel_list[i])):
#                 if pixel_list[i][j][3] == 0:
#                     background_color_list.append(pixel_list[i][j])
#         return background_color_list
#     return find_most_common_color(image)


# def is_background_color(pixel, background_color):
#     if isinstance(background_color, set):
#         return pixel in background_color
#     return np.all(pixel == background_color)


# if __name__ == "__main__":
#     image = SpriteSheet("./img/Brightness/camera.jpg")
#     new_image = image.create_sprite_labels_image()
#     new_image.save("./img/Brightness/camera.jpg")



def check_file_exist(path):
    try:
        with open(path, 'rb') as image_file:
            image = face_recognition.load_image_file(image_file)
            return image
    except OSError:
        pass


def find_most_common_color(image):
        color_count = defaultdict(int)
        for pixel in image.getdata():
            color_count[pixel] += 1
        return max(color_count.items(), key=operator.itemgetter(1))[0]
        print(find_most_common_color)
find_most_common_color("./img/Brightness/camera.jpg")