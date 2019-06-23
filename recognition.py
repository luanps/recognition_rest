# -*- coding: utf-8 -*-
import json
import base64
import cv2

class Recognition:
    """Recognition"""

        def __init__(self,params: dict) -> result: dict:

            self.request_number = params['request_number']
            self.id = params['id']
            self.input_image = params['input_image']
            self.action = params['action']

    
        def convert_base64_to_img(img_b64):

            if ',' in img_b64:
                img_b64 = self['input_image'].split(',')[-1]
                
            img_b64 = base64.b64decode(img_b64)
            img_b64 = np.frombuffer(img_b64,dtype = np.uint8)
            img = cv2.imdecode(img_b64,flags=1)

            return img    


        def convert_img_to_base64(img):

            _, img_b64(cv2.imencode('.jpg',img)

            return base64.b64encode(img_b64)

