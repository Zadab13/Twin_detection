import cv2 as cv

# hier worden de kaders rond de 2 gezichten getekent
# X haalt het eerste element uit de lijst best en Y het tweede
# de kleur en dikte van de kaders worden bepaalt 
# het eerste kader komt rond gezicht x en het tweede rond gezicht Y
# de rest van de code komt overeen met die van pic_read


def draw_frames(img, best, boxes):
    X = best[0]
    Y = best[1]
    COLOR = (0,255,0)
    THICKNESS = 3

    box_1 = boxes [X]
    box_2 = boxes [Y]
    
    (top, right, bottom, left) = box_1
    start_point = (left, top)
    end_point = (right, bottom)
    cv.rectangle(img, start_point, end_point, COLOR, THICKNESS)

    (top, right, bottom, left) = box_2
    start_point = (left, top)
    end_point = (right, bottom)
    cv.rectangle(img, start_point, end_point, COLOR, THICKNESS)
    