import os
import imgaug as ia
import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import load
import tools
import coordinate
import img_aug_tool
import save
import cv2

image_load_path = "/home/gsh/PycharmProjects/PycharmProjects/PycharmProjects/img_aug/train_img"
text_load_path = "/home/gsh/PycharmProjects/PycharmProjects/PycharmProjects/img_aug/train_txt"
image_result_path = "/home/gsh/PycharmProjects/PycharmProjects/PycharmProjects/img_aug/result_img"
text_result_path = "/home/gsh/PycharmProjects/PycharmProjects/PycharmProjects/img_aug/result_txt"

image_names = load.load_img_names(image_load_path)
num = 10  # 生成数据的数量
data_number = 0  # 计数器
while True:

    # 设置索引号
    index = tools.rand_int(num)
    # 设置路径
    image_path = os.path.join(image_load_path, image_names[index])
    text_path = os.path.join(text_load_path, image_names[index][:-3] + "txt")
    # 读图
    image, h, w = load.img_read(image_path)
    # 读txt
    text = load.txt_read_alllines(text_path)
    # 分离label 和坐标
    label_list, coordinate_before_list = coordinate.txt_separate(text, h, w)
    # 变换图像
    image_aug, bbs_aug = img_aug_tool.img_aug(image, coordinate_before_list, h, w)
    # 变换后图像的坐标
    coordinate_after_list = coordinate.get_coordinate_after(bbs_aug)
    # 标志位判断是否被裁
    flag = 0
    # 写入的内容
    content = ""
    # 遍历框框
    for i in range(len(coordinate_before_list)):
        # 变换后框的面积
        area = tools.get_area(coordinate_after_list[i])
        # 剪裁框框的坐标--和--剪裁后框框的面积
        cut_area, cut_coordinate_list = tools.cut_box(coordinate_after_list[i], h, w)
        # 写入的内容
        content = content + save.write_content(label_list[i],
                                               coordinate.coordinate_translate_r(cut_coordinate_list, h, w))
        # 判断裁掉剩下的面积是否大于原先的85%
        if cut_area < area * 0.85:
            flag = 1
            break
    # 不够85%就进行下一张图
    if flag == 1:
        continue
    else:
        # 85%以上的保存图像和TXT
        data_number += 1
        save_text_name = os.path.join(text_result_path,
                                      "-{}-change_{}".format(data_number, image_names[index][:-3] + "txt"))
        save.save_txt(name=save_text_name, content=content)
        save_image_name = os.path.join(image_result_path, "-{}-change_{}".format(data_number, image_names[index]))
        save.save_img(img_name=save_image_name, img=image_aug)

    # 数量达到，结束程序
    if data_number == num:
        break
