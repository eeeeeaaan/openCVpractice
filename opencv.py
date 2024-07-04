import cv2
import numpy as np
#예제 2-3 이미지를 그레이스케일로 저장

img_file='PrettyGirl.jpeg'
img= cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else: 
    print("No image file.")

#2-5 카메라 프레임 읽기 -> no frame
cap= cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera', img)
            if cv2.waitKey(1) != -1 :
                break
        else: 
            print("no frame")
            break
else:
    print("can't open camera")
cap.release()
cv2.destroyAllWindows() 
        
# 2-9 카메라로 녹화하기
if cap.isOpened():
    file_path= 'record1.avi'
    fps= 30.0
    fourcc= cv2.VideoWriter_fourcc(*'DIVX')
    width= cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height= cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size= (int(width), int(height))
    out= cv2.VideoWriter(file_path, fourcc, fps, size) #이게 레코딩을 담는 상자
    while True:
        ret, frame= cap.read()
        if ret:
            cv2.imshow('recording', frame)
            out.write(frame)
            if cv2.waitKey(int(1000/fps)) != -1:
                break
        else:
            print("no frame")
            break
    out.release()
else:
    print("can't open camera")
cap.release()
cv2.destroyAllWindows()

# 2-10 그려보기
img= np.full((500,500,3), 255, dtype= np.uint8)
cv2.imwrite('blank.jpg', img)
cv2.line(img, (50,50), (150, 50), (255, 0,0))   
cv2.rectangle(img, (200, 200),(250,250), (0,255,0), -1)         
cv2.imshow('line', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2-17 마우스 이벤트 다루기
title= 'mouse event'
img= cv2.imread('blank.jpg')
cv2.imshow(title, img)

def onMouse(event, x, y, flags, param):
    print(event, x,y,)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 30, (0,0,0), -1)
        cv2.imshow(title, img)
cv2.setMouseCallback(title, onMouse)

while True:
    if cv2.waitKey(0) & 0xFF  ==27:
        break
cv2.destroyAllWindows()