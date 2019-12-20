import argparse
import cv2
import face_recognition


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

file = open("./img/Brightness/camera.jpg", "wb")
print("Tên của file là: ", file.name)
print("File đóng hoặc không? : ", file.closed)
print("Chế độ mở file : ", file.mode)

cv2.imshow("Image", image) # show img
cv2.imwrite("./img/Brightness/camera.jpg", image) # save img
cv2.waitKey(0)
# RUNNN  python ham_chinh.py -i ./img/Brightness/camera.jpg


# def check_file_exist():
# try:
#     with open(path, 'rb') as image_file:
#         image = face_recognition.load_image_file(image_file)
#         return image
# except IOError:
#     print("File not valid")



