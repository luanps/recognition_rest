# -*- coding: utf-8 -*-
import json
import base64
import cv2
import numpy as np

class Recognition:
    """Recognition"""

    def __init__(self,params: dict):

        self.request_number = params['request_number']
        self.id = params['id']
        self.img_b64 = params['img_base64']
        self.action = params['action']


    def convert_base64_to_img(self):
        
        img_b64 = self.img_b64
        #if ',' in img_b64:
        #    img_b64 = img_b64.split(',')[-1]
            
        img_b64 = base64.b64decode(img_b64)
        img_b64 = np.frombuffer(img_b64,dtype = np.uint8)
        self.img = cv2.imdecode(img_b64,flags=1)


    def convert_img_to_base64(self):

        _, img_b64 = cv2.imencode('.jpg',self.input_image)
        self.img = base64.b64encode(img_b64)
