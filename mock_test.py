from main import main
import cv2
import base64

def convert_img_to_base64(img):
    _, img_b64 = cv2.imencode('.jpg',img)
    return base64.b64encode(img_b64)

img = cv2.imread("luan.jpg")
img_b64 = convert_img_to_base64(img)

data = {
    "request_number": 123,
    "id": 444555,
    "action":0,
    "img_base64":img_b64
    }

main(data)
        
