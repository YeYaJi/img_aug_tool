import os
import imgaug as ia
import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage

import os
import cv2

def load_img_names(path):
    names_list = os.listdir(path=path)
    return names_list


def img_read(name_path):
    img = cv2.imread(name_path)
    h, w, c = img.shape
    return img, h, w


def txt_read_alllines(txt_path):
    with open(txt_path, "r") as f:
        all_lines = f.readlines()
    return all_lines