import face_recognition as fr
# 2. facematch.py

def compare_faces(file1, file2):
    # Load the jpg files into numpy arrays
    # file1 = './img/known/massu.jpg'
    # file2 = './img/unknown/massu_31.jpg'
    image1 = fr.load_image_file(file1)
    image2 = fr.load_image_file(file2)

    # Get the face encodings for 1st face in each image file
    image1_encoding = fr.face_encodings(image1)[0]
    image2_encoding = fr.face_encodings(image2)[0]
    
    # Compare faces and return True / False
    results = fr.compare_faces([image1_encoding], image2_encoding)  
    if results[0]:
        return 'This is Massu cute'
    else:
        return 'This is not Massu cute'


def main():
    file1 = './known/massu.jpg'
    file2 = './unknown/massu_31.jpg'
    print(compare_faces(file1, file2))


if __name__ == "__main__":
    main()