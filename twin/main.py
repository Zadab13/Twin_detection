# we importeren alle gemaakte functies en argparse
import argparse
from pic_read import read_image_from_file, resize_pic
from face_det import face_detection #draw_boxes
from face_feat import face_features
from face_com import face_comparison
from filter import find_best
from output import show_image
from draw import draw_frames

# hier wordt de grootte van de afbeelding bepaalt
COMPUTE_WIDTH = 2048
DISPLAY_WIDTH = 712

# deze functie analyseert de argumenten die zijn ingegeven wanneer het programma wordt opgestart 
# in dit geval, het file path van de gegeven afbeelding
# als er niets wordt ingegeven zal het bericht "input file containing an image" worden getoont
def analyse_args():
    parser = argparse.ArgumentParser(
        description="Twin detection system")
    parser.add_argument('-i', '--input-file', required=True, help="Input file containing an image")

    args = parser.parse_args()
    return args

# twin_det wordt aangeroepen uit main, hierin gebeurt het hele vergelijkingsprocess van de gezichten
# op het einde krijg je de twee gezichten waar kaders rond gaan terug
def twin_det(img):
    boxes = face_detection(img)
    #img_w_boxes = draw_boxes(img, boxes)
    encodings = face_features(boxes, img)
    matches = face_comparison(encodings)
    best = find_best(matches)
    draw_frames(img, best, boxes)

# de functie main begint wanneer het porgramma start en roept de verschillende onderdelen aan
# het eindigt met de output van de afbeelding met de 2 kaders op
def main ():
    args = analyse_args()
    img = read_image_from_file(args.input_file)
    new_img = resize_pic(img, COMPUTE_WIDTH)
    twin_det(new_img)
    output_img = resize_pic(new_img, DISPLAY_WIDTH)
    show_image(output_img)



# Dit zorgt ervoor dat wanneer 
if __name__ == "__main__":
    main()
