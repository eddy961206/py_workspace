import cv2
import numpy as np
# https://developtogether.tistory.com/entry/ROS-OpenCV-%EA%B8%B0%EC%B4%88-Python


img = cv2.imread('gta5/loopy.jpg',cv2.IMREAD_COLOR)             # 이미지 읽기
# img = cv2.imread('gta5/loopy.jpg',cv2.IMREAD_GRAYSCALE)       # 흑백으로 읽기
if img is None:
    print('Image load failed')
    exit()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_white = np.array([0,0,220]) # np.array[H(0~150), S(0~255), V(220~255)] Value:명도. 255에 가까울수록 흰색과 가까운 것만 표시
upper_white = np.array([150,255,255])

mask = cv2.inRange(hsv, lower_white, upper_white)
cv2.imshow('hsv', mask)
cv2.waitKey(5000)

exit()


img = cv2.circle(img, (180,180), 100, (255,255,255), 10)
img = cv2.rectangle(img,(0,0), (300,300),(255,255,255),8)
img = cv2.line(img, (0,0), (300,300),(255,255,255), 16)

#1번
print("height : ", len(img))  # height 크기
print("width : ", len(img[0]))  # width 크기

#2번
print("색깔 : ", img[0,0]) # img[height, width] 색깔
print("색깔 : ", img[420,0]) # -> 0,420 좌표의 색깔

print(img.shape)
cv2.imshow('ROI', img[300:450,0:640])
cv2.imshow('circle in loopy', img) # 읽은 이미지를 보여주기
cv2.waitKey(5000)