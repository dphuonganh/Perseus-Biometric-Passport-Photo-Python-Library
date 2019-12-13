import face_recognition
# 1. findfaces.py

image = face_recognition.load_image_file('./img/groups/team1.jpg')
face_locations = face_recognition.face_locations(image)

# Mảng coords của mỗi khuôn mặt
# print(face_locations)

# Đếm số người có mặt trong tấm ảnh
# print(f'There are {len(face_locations)} people in this image')