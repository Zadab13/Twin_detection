# In dit deel van de code wordt een gegeven afbeelding gelezen vanaf een file path. het tweede deel 
# van de code zortgt ervoor dat we de afbeelding kunnen vervormen naar een gewenste formaat.

# importeer volgende libraries: cv2 en os
import cv2 as cv
import os

# Hier definieren we de functie read_image from_file met als argument file_path , hiervoor gebruiken 
# we een functie uit cv namelijk cv.imread(file_path) als de gegeven file_path niet gevonden is zal de functie 
# "image not found" afprinten en het programma stoppen.
def read_image_from_file(file_path):
    img = cv.imread(file_path)
    if not os.path.exists(file_path):
        print("image not found")
        exit()
    return img

# Dit is de functie resize_pic met als argumenten img en desired_width om de foto te hervormen wordt er eerst 
# de ratio tussen de breedte en de hoogte achterhaald om dan op basis van de gewenste breedte de gewenste 
# hoogte achterhalen. Uiteindelijk word de functie cv.resize(img, (desired_width, desired_height)) gebruikt 
# om een nieuwe hoogte en breedte toe te eigenen aan de afbeelding.
def resize_pic(img, desired_width):
    aspect_ratio = img.shape[1] / img.shape[0]
    desired_height = int(desired_width / aspect_ratio)
    resized_img = cv.resize(img, (desired_width, desired_height))
    return resized_img
