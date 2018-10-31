#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
import HyperLPRLite as pr

# import csv

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
# fontC = ImageFont.truetype("./Font/platech.ttf", 14, 0)

import cv2

def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),cv2.IMREAD_UNCHANGED)
    return cv_img

# def drawRectBox(image,rect,addText):
#     cv2.rectangle(image, (int(rect[0]), int(rect[1])), (int(rect[0] + rect[2]), int(rect[1] + rect[3])), (0,0, 255), 2,cv2.LINE_AA)
#     cv2.rectangle(image, (int(rect[0]-1), int(rect[1])-16), (int(rect[0] + 115), int(rect[1])), (0, 0, 255), -1,
#                   cv2.LINE_AA)
#     img = Image.fromarray(image)
#     draw = ImageDraw.Draw(img)
#     draw.text((int(rect[0]+1), int(rect[1]-16)), addText, (255, 255, 255), font=fontC)
#     # draw.text((int(rect[0]+1), int(rect[1]-16)), addText.decode("utf-8"), (255, 255, 255), font=fontC)
#     imagex = np.array(img)
#     return imagex


# parent= r"images\xingneng\分辨率变化子库"
# parent= r"images\special\新能源-大车牌"
# parent= r"images\plate-data"


# list = 'images/here/京A88731.jpg'
# list2 = 'images_rec/2_.jpg'
# list3 = list.encode('gbk')
# image =  cv_imread(list)
# print(type(image))
# cv2.imshow("image",image)
model = pr.LPR("model/cascade.xml","model/model12.h5","model/ocr_plate_all_gru.h5")

filename_list = []
predict_list = []
colors_list = []

def plate_recogniton(real_path):
    if 'img_test'in real_path:
        plate_real = 'img_test' + real_path.split('img_test')[-1]
    else:
        plate_real = real_path.split('img_test')[-1]
    filename_list.append(plate_real)
    print('plate_real:' + str(plate_real))

    if real_path.endswith(".jpg") or real_path.endswith(".png") or real_path.endswith(".JPG"):
        image =  cv_imread(real_path)
        # print(type(image))
        # image,res  = model.SimpleRecognizePlateByE2E(image)
        res = model.SimpleRecognizePlateByE2E(image)
        max_res = ['null',0,[862.01999999999998, 924.0, 178.03504678726196, 52.0]]
        res.sort(key=lambda x: x[1],reverse=True)
        if len(res) == 0:
            pass
        elif len(res) >= 1:
            max_res = res[0]
        print(res)
        color = res[0][-1]
        plate_predict = max_res[0]
        print('plate_predict:' + plate_predict)
        print('color:' + color)
        predict_list.append(plate_predict)
        colors_list.append(color)

import os

def batch_main(parent):
    for fpathe, dirs, fs in os.walk(parent):
        for f in fs:
            filepath = os.path.join(fpathe, f)
            plate_recogniton(filepath)

    print(filename_list)
    print(colors_list)
    print(predict_list)
    return filename_list, colors_list, predict_list






