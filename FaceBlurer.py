from PIL import Image, ImageFilter
import face_recognition
import sys
import random

#we input the absolute path to a photo we desire to edit

path = input('Post a desired photo absolute path: \n')

try:
    image = face_recognition.load_image_file(str(path))
except FileNotFoundError:
    print('Error: Wrong path or file non-existent')
    sys.exit()

#we form a picture to edit

pilImage = Image.fromarray(image)

#use face_recognition module to find faces and a simple for loop to crop them, blur them and paste them back on the original photo

face_locations = face_recognition.face_locations(image)

for face_location in face_locations:
    top,right,bottom,left = face_location
    box = (left,top,right,bottom)
    blur = pilImage.crop(box).filter(ImageFilter.BoxBlur(10))
    pilImage.paste(blur, box)

#we then save the edited photo

path2 = input('Done. Post the desired blured photo container absolute path: \n')

num = random.randint(1, 10000)

try:
    pilImage.save(str(path2) + str(num) + '.jpg')
    print('Your photo is saved')
except:
    print('Failed to save photo, check your path.')

