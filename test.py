import os.path
from os import path


def main():
    """
        @param: The file contains photos

        @return: Check the path file whether it exists or not
    """
    im = Image.open("./img/Brightness/camera.jpg")

    # Check the path file whether it exists or not
    print ("file exist:"+str(path.exists('./img/groups/team1.jpg')))
    print ("File exists:" + str(path.exists('./img/groups/team1.pdf')))
    print ("Directory exists:" + str(path.exists('./img/Brightness/camera.jpg')))

    # To check if the path points to a directory or not
    print ("Is it Directory?" + str(path.isdir('./img/Brightness/camera.jpg')))
    print ("Is it Directory?" + str(path.isdir('./img')))


if __name__== "__main__":
   main()