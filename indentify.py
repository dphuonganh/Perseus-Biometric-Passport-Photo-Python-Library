import face_recognition
from PIL import Image, ImageDraw

image_of_bill = face_recognition.load_image_file('./img/known/bill-gates.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

image_of_steve = face_recognition.load_image_file('./img/unknown/steven-jobs.jpg')
steve_face_encoding = face_recognition.face_encodings(image_of_steve[0])

# create array of encodings and names (tạo mảng mã hóa và tên)
known_face_encodings = [
    bill_face_encoding,
    steve_face_encoding
]

known_face_names = [
    "Bill Gates",
    "Steve Jobs"
]

# Load test image to find faces in (Tải hình ảnh thử nghiệm để tìm khuôn mặt trong)
test_image = face_recognition.load_image_file('./img/groups/bill-steve.jpg')

# find faces in test image (Tìm ảnh gương mặt trong ảnh thử nghiệm)
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format (Chuyển đổi sang định dạng PIL)
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image (Lặp lại qua các khuôn mặt trong hình ảnh thử nghiệm)
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    print(known_face_encodings)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(face_encodings)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    # If it match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    
    # Draw Box
    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0),
    outline=(0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

del draw

# Display image
pil_image.show()