from PIL import Image
import face_recognition
'''
3. pullfaces.py
Đây là function để cắt ảnh từng gương mặt cụ thể
'''

image = face_recognition.load_image_file('./img/groups/team1.jpg')
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:
    top, right, bottom, left = face_location

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    # pil_image.show()
    pil_image.save(f'{left}.jpg') # can change