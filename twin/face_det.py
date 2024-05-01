# In dit deel van de code worden de verschillende gezichten herkent.

# Importeer volgende libraries: cv2 en face_recognition.
import cv2 as cv
import face_recognition

# Deze variabelen bepalen de kleur en de breedte van de rechthoeken die 
# getekend zullen worden.
COLOR = (0, 0, 255)
THICKNESS = 2

# De functie face_detection met als argument img zal gebruik maken van 
# de functie face_recognition.face_locations() om ons een lijst te geven 
# met tuples die de coördinaten bevatten van de boxes die getekend zullen worden.
def face_detection (img):
    boxes = face_recognition.face_locations(img)
    return boxes


# Deze functie word niet echt gebruikt in het programma. 
# Deze werd geschreven om te controleren of het bovenste deel van de code werkt. 
# Dezelfde code wordt wel gebruikt verder in de code namelijk in draw.py.
# In de functie wordt er eerst een copie gemaakt van de afbeelding, dan wordt er een lus 
# gemaakt waarin er voor elk element in de lijst "boxes" de coördinaten worden achterhaalt 
# en op basis van de coördinaten een start en eind punt bepaald wordt. De functie cv.rectangle() 
# zal dan met de opgegeven coördinaten van de startunt en de eindpunt op de kopie van de afbeelding rechthoeken tekenen.
def draw_boxes(img, boxes):
    img_copy = img.copy()
    for box in boxes:
        (top, right, bottom, left) = box
        start_point = (left, top)
        end_point = (right, bottom)
        cv.rectangle(img_copy, start_point, end_point, COLOR, THICKNESS)
    return img_copy
