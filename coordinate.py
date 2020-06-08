import os
import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage


def coordinate_translate(coordinate_yolo_list, h, w):

    x = (float(coordinate_yolo_list[0]) * w)
    y = (float(coordinate_yolo_list[1]) * h)
    box_w = (float(coordinate_yolo_list[2]) * w)
    box_h = (float(coordinate_yolo_list[3]) * h)
    x1 = x - box_w / 2
    y1 = y - box_h / 2
    x2 = x + box_w / 2
    y2 = y + box_h / 2
    coordinate_list = [x1, y1, x2, y2]
    return coordinate_list


def coordinate_translate_r(coordinate_normal_list, h, w):
    box_w = abs(coordinate_normal_list[0] - coordinate_normal_list[2])
    box_h = abs(coordinate_normal_list[1] - coordinate_normal_list[3])
    x1 = abs(coordinate_normal_list[0]+ box_w / 2) / w
    y1 = abs(coordinate_normal_list[1] + box_h / 2) / h
    x2 = abs(box_w/w)
    y2 = abs(box_h/h)
    coordinate_list = [x1, y1, x2, y2]
    return coordinate_list


def txt_separate(txt_all_in_list, h, w):
    label_list = []
    coordinate_list = []
    for line in txt_all_in_list:
        line = line.strip("\n")
        line_list = line.split(" ")
        label_list.append(line_list[0])
        coordinate_before_list = [line_list[1], line_list[2], line_list[3], line_list[4]]
        coordinate_normal_list = coordinate_translate(coordinate_before_list, h, w)
        coordinate_list.append(coordinate_normal_list)
    return label_list, coordinate_list


def get_coordinate_after(bbs_aug):
    coordinate = []
    for after in bbs_aug.bounding_boxes:
        coordinate.append([after.x1, after.y1, after.x2, after.y2])
    return coordinate


if __name__ == "__main__":
    with open("/home/gsh/PycharmProjects/PycharmProjects/PycharmProjects/img_aug/1328764596424542194.txt", "r")as f:
        m = f.readlines()
    # print(m)
    # m=['4 0.5864075660705567 0.16611369450887045 0.05330663323402405 0.11288074917263455\n', '0 0.648325252532959 0.16646528244018555 0.04972551763057709 0.12847351498074003\n', '4 0.5254065990447998 0.1665802001953125 0.05280252695083618 0.11433419121636285\n', '4 0.4629537105560303 0.16459506352742512 0.052631109952926636 0.10916645261976454\n']

    a, b = txt_separate(m, 720, 1280)
    print(a)
    print("\n\n")
    print(b)
