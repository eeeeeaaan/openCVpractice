import numpy as np
import cv2
import matplotlib.pyplot as plt

# #3.1.14 이미지 생성
# img = np.zeros((120, 120), dtype= np.uint8)
# img[25:35,:] =45
# img[55,65,:] =115 # 이렇게 값을 할당하는 것 뿐만 아니라  rgb 스케일로도 할당 가능함
# img[85,95,:]= 160
# img[:,35,45] = 205
# img[:, 75,85]= 255
# cv2.imshow('Gray', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# matplotlib 활용하기 
img1= cv2.imread('PrettyGirl.jpeg')
img2= cv2.imread('busyStreet.jpeg')

plt.subplot(221)
plt.imshow(img1[:,:,::-1]) 

plt.subplot(222)
plt.imshow(img2)

plt.show()
# 이 때 이미지가 이상하게 나오는데 원래는 rgb로 읽혀야하는데 opencv이미지는 bgr 순으로 읽기 때문이다. 
# 그래서 img[:,:,::-1]을 해준 이미지를 넣어야한다. 