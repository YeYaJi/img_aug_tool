import os
import cv2


def write_content(label, coordinates)->str:
    content = label
    for i in coordinates:
        i = str(i)
        content = content + " " + i
    else:
        content = content + "\n"
    return content


def save_txt(name: str, content: str) -> None:
    with open(name, "w") as f:
        f.write(content)


def save_img(img_name, img):
    cv2.imwrite(img_name, img)
