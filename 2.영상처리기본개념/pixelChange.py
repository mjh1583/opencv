import cv2 as cv
import numpy as np

img_color = cv.imread("D:/opencv-test/2.영상처리기본개념/test.jpg", cv.IMREAD_COLOR)

# 이미지의 높이와 너비를 가져옴
height, width = img_color.shape[:2]

# 그레이 스케일 이미지를 저장할 넘파이 배열을 생성
img_gray = np.zeros((height, width), np.uint8)

# for문을 돌면서 (x, y)에 있는 픽셀을 하나씩 접근
for y in range(0, height):
    for x in range(0, width):

        # openCV는 rgb채널이 아닌 bgr채널
        # 컬러 이미지의 (x, y)에 있는 픽셀의 b,g,r 채널 읽음
        b = img_color.item(y, x, 0)
        g = img_color.item(y, x, 1)
        r = img_color.item(y, x, 2)

        # (x, y)위치의 픽셀에 그레이 스케일 값이 저장
        # 평균값 사용하는 경우 (비추천)
        # gray = int((r + g + b) / 3)
        # BT.709에 명시된 비율을 사용하는 경우
        gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)

        img_gray.itemset(y, x, gray)

# 결과 이미지에 컬러를 표시하기 위해 컬러 이미지로 변환
img_result = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)

# y 범위가 150~200, x 범위가 200~250인 영역의 픽셀을 초록색 픽셀로 변환
for y in range(150, 201):
    for x in range(200, 251):

        img_result.itemset(y, x, 0, 0)  # b 
        img_result.itemset(y, x, 1, 255)  # g
        img_result.itemset(y, x, 2, 0)  # r

cv.imshow("img_color", img_color)
cv.imshow("img_result", img_result)
cv.imshow("img_gray", img_gray)

cv.waitKey(0)

cv.destroyAllWindows()