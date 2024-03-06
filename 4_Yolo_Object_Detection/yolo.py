#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dashnisan
"""
########################################################################################

import marshal
import argparse
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import scipy.io
import scipy.misc
import numpy as np
import pandas as pd
import PIL
from PIL import ImageFont, ImageDraw, Image
import tensorflow as tf
from tensorflow.python.framework.ops import EagerTensor

from tensorflow.keras.models import load_model
from yad2k.models.keras_yolo import yolo_head
from yad2k.utils.utils import draw_boxes, get_colors_for_classes, scale_boxes, read_classes, read_anchors, preprocess_image

########################################################################################
# load code in .pyc

s = open('yolo_functions.cpython-38.pyc', 'rb')
s.seek(16)  # go past first eight bytes
code_obj = marshal.load(s)
exec(code_obj)



########################################################################################
# load pre-trained yolo model

class_names = read_classes("model_data/coco_classes.txt")
anchors = read_anchors("model_data/yolo_anchors.txt")
model_image_size = (608, 608) # Same as yolo_model input layer size
yolo_model = load_model("model_data/", compile=False)
yolo_model.summary()

########################################################################################
# predict on test pictures:

for testpic in ['bikes.jpg','cars1.jpg','cars_dump.jpg','motorbikes.jpg', 'roundabout.jpg',
               'trucks.jpg']:
    out_scores, out_boxes, out_classes = predict(testpic)


########################################################################################


