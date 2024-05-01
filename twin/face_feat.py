# In dit deel van de code worden de kenmerken van de gezichten gedetecteerd en opgeslagen in een nieuwe lijst.

# Importeer face_recognition
import face_recognition

# De functie face_feutures met als argumenten boxes en img zal met de functie face_recognition.face_encodings() 
# een nieuwe lijst maken met alle "encodings", de kenmerken van de gezichten.
def face_features (boxes, img):
    encodings = face_recognition.face_encodings(img, boxes)
    return encodings
