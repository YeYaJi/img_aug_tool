import random


def rand_int(num):
    x = random.randint(0, num)
    return x


def get_area(coordinate_list):
    area = abs(coordinate_list[0] - coordinate_list[2]) * abs(coordinate_list[1] - coordinate_list[3])
    return area


def cut_box(after_coordinate_list, h, w):
    for i, coordinate in enumerate(after_coordinate_list):
        if coordinate < 0:
            after_coordinate_list[i] = 0
        elif coordinate > w:
            if i == 0 or i == 2:
                after_coordinate_list[i] = w
            else:
                after_coordinate_list[i] = h
        elif coordinate > h:
            if i == 1 or i == 3:
                after_coordinate_list[i] = h
    after_cut_coordinate_list = after_coordinate_list
    after_cut_area = get_area(after_cut_coordinate_list)

    return after_cut_area, after_cut_coordinate_list
