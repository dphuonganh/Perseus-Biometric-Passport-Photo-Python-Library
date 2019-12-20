import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width: %d pixels" % (image.shape[1]))
print("height: %d pixels" % (image.shape[0]))
print("channels: %d channels" % (image.shape[2]))

cv2.imshow("Image", image) # show img
cv2.imwrite("./img/Brightness/camera.jpg", image) # save img
cv2.waitKey(0)
# RUNNN  python chinh_sang.py -i ./img/Brightness/camera.jpg


def get_photo_hint(path):
    """Detect crop hints on a single image and return the first result."""
    with io.open(path, 'rb') as image_file:
        try: 
            images = face_recognition.load_image_file(image_file)
            return images
        except IOError: 
            pass


def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()