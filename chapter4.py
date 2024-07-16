import cv2
import numpy as np
import matplotlib.pylab as plt
# #4-2
# img= cv2.imread('PrettyGirl.jpeg')
# x= 340
# y=200
# w=100
# h=50
# roi= img[y:y+h, x:x+w]
# print(roi.shape)
# cv2.rectangle(roi, (0,0),(h-1,w-1), (0,255,0))
# cv2.imshow('Img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #4-3 마우스로 관심영역 지정하기
# isDragging= False
# x0, y0 , w,h= -1, -1, -1, -1
# blue, red = (255,0,0) , (0,0,255)

# def onMouse(event, x, y, flags, param):
#     global isDragging, x0, y0, img
#     if event== cv2.EVENT_LBUTTONDOWN:
#         isDragging = True
#         x0= x 
#         y0=y
#     elif event== cv2.EVENT_MOUSEMOVE:
#         if isDragging:
#             img_draw = img.copy()
#             cv2.rectangle(img_draw, (x0, y0),(x,y), blue, 2)
#             cv2.imshow('img', img_draw)
#     elif event== cv2.EVENT_LBUTTONUP:
#         if isDragging:
#             isDragging = False
#             w= x-x0
#             h= y- y0
#             print("x:%d, y:%d, w:%%d, h:%d" % (x0, y0, w,h))
#             if w> 0 and h>0:
#                 img_draw = img.copy()
#                 cv2.rectangle(img_draw, (x0, y0),(x,y), red, 2)
#                 cv2.imshow('img', img_draw)
#                 roi= img[y0: y0+h, x0: x0+w]
#                 cv2.imshow('cropped' , roi)
#                 cv2.moveWindow('cropped', 0,0)
#                 print("cropped")
                
#             else:
#                 cv2.imshow('img', img)
#                 print("좌측 상단에서 우측 하단으로 영역을 드래그 하세요.")
                
# img = cv2.imread('PrettyGirl.jpeg')
# cv2.imshow('img', img)
# cv2.setMouseCallback('img', onMouse)
# cv2.waitKey()
# cv2.destroyAllWindows()

# # 이미지 합성과 마스킹 
# img_fg= cv2.imread('PrettyGirl.jpeg', cv2.IMREAD_UNCHANGED)
# img_bg= cv2.imread('busyStreet.jpeg')

# _, mask= cv2.threshold(img_fg[:,:,3], 1,255, cv2.THRESH_BINARY)
# mask_inverse= cv2.bitwise_not(mask)

# # 히스토그램 나타내기 
# img = cv2.imread('PrettyGirl.jpeg')
# hist1= cv2.calcHist(img,[1], None, [ 256], [0,256] )
# hist0= cv2.calcHist(img,[0], None, [ 256], [0,256] )
# hist2= cv2.calcHist(img,[2], None, [ 256], [0,256] )
# plt.plot(hist1, color='g')
# plt.plot(hist0, color= 'b')
# plt.plot(hist2, color= 'r')
# plt.show()
# hist = cv2.calcHist([img], [0, 1], None, [32, 32], [0, 256, 0, 256])
# plt.plot(hist)
# plt.show()

# 정규화를 통한 화질 개선 

img = cv2.imread('smokePicture.jpg', cv2.IMREAD_GRAYSCALE)
img_norm= cv2.normalize(img,None,0, 255, cv2.NORM_MINMAX)
# img_norm_l1= cv2.normalize(img , 1, 0, cv2.NORM_L1) 실패
# img_norm_l2= cv2.normalize(img, None , 1, 0, cv2.NORM_L2) 실패
# img_norm_inf= cv2.normalize(img, None , 0, 255, cv2.NORM_INF) 실패

hist= cv2.calcHist([img], [0], None, [256], [0,255])
hist_norm_minmax= cv2.calcHist([img_norm], [0], None, [256], [0,255])
cv2.imshow('before', img)
cv2.imshow('after', img_norm)
# cv2.imshow('l1', img_norm_l1)
# cv2.imshow('l1', img_norm_l2)
# cv2.imshow('l1', img_norm_inf)
cv2.waitKey()
cv2.destroyAllWindows()
hists= { 'before': hist, 'after': hist_norm_minmax }
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1,2,i+1)
    plt.title(k)
    plt.plot(v)
plt.show()


# # 이퀄라이즈 예제 (어두움 개선)
# img= cv2.imread('aqua.jpg')
# img= cv2.resize(img, dsize=(400, 600), interpolation=cv2.INTER_AREA)

# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
 
# img1[:,:,0] = cv2.equalizeHist((img1[:,:,0]))
# img2= cv2.cvtColor(img1, cv2.COLOR_YUV2BGR)
# numpy_horizontal = np.hstack((img, img2))

# cv2.imshow('Before', numpy_horizontal)

# cv2.waitKey()
# cv2.destroyAllWindows()
