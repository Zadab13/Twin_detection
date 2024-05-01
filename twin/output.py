import cv2 as cv

# dit is de output van het programma
# de afbeelding wordt getoond met 2 kaders rond de 2 meest gelijkende gezichten.
# de cv.imshow toont de afbeelding met daarboven de tekst "display window"
# de fucntie waitKey zorgt ervoor dat het programma dan afsluit wanneer er op 0 wordt gedrukt.

def show_image(img):
    cv.imshow("Display window", img)
    cv.waitKey(0)

    

