import os
import imgaug as ia
import cv2
import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage


def img_aug(image, coordinate_lists, h, w):
    BoundingBox_list = []
    for coordinate in coordinate_lists:
        BoundingBox_list.append(
            BoundingBox(x1=coordinate[0], y1=coordinate[1], x2=coordinate[2],
                        y2=coordinate[3]))

    bbs = BoundingBoxesOnImage(BoundingBox_list, (h, w))
    seq = iaa.Sequential([

        iaa.ChangeColorTemperature((3000, 40000)),
        iaa.Affine(translate_px={"x": (-150, 150), "y": (-150, 150)}, scale=(0.5, 1.7), rotate=(-15, 15))

    ])
    image_aug, bbs_aug = seq(image=image, bounding_boxes=bbs)
    return image_aug, bbs_aug


if __name__ == "__main__":
    coordinate = [[716.4854393005371, 78.96479034423828, 784.7179298400879, 160.23892974853516],
                  [798.0319919586182, 73.60453796386719, 861.6806545257568, 166.10546875],
                  [638.7268295288086, 78.77743530273438, 706.3140640258789, 161.09805297851562],
                  [558.8968391418457, 79.20852279663085, 626.2646598815918, 157.80836868286133]]

    image = cv2.imread("/home/gsh/PycharmProjects/PycharmProjects/PycharmProjects/img_aug/1328764596424542194.jpg", 1)
    img_aug()