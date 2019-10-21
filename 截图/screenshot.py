# pip3 install opencv-python

# 调用摄像头，拍照
import cv2
#屏幕截图
from PIL import ImageGrab

#屏幕截图
def captuer():
    #截取屏幕
    im = ImageGrab.grab()
    im.save('scrang.png')

# 调用系统摄像头，拍照
def photo():
    #调用摄像头0
    cap = cv2.VideoCapture(0)
    #读取摄像头的内容,第一个值是否读取成功，第二个值，读取的资源
    ret,img = cap.read()
    if ret:
        cv2.imwrite('photograph.jpg',img)
    #释放
    cap.release()

captuer()
photo()