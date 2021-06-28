import cv2 as cv
import sys

img_color = cv.imread("D:/opencv-test/3.그래픽사용자인터페이스/ball.png", cv.IMREAD_COLOR)

if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    sys.exit(1)

# 그레이 스케일 이미지로 변환
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

# Canny를 사용하여 에지 검출
img_canny = cv.Canny(img_gray, 90, 180)

# 윈도우별로 처리 결과를 보여줌
# cv.imshow("GrayScale", img_gray)
# cv.imshow("Canny", img_canny)

# cv.waitKey(0)
# cv.destroyAllWindows()

# 연결할 이미지를 hconcat, vconcat의 아규먼트로 입력
# 같은 타입의 이미지여야 함

# 수평 방향으로 matrices에 포함된 이미지 연결
img_result = cv.hconcat([img_gray, img_canny])

# 수직 방향으로 matrices에 포함된 이미지 연결
# img_result = cv.vconcat([img_gray, img_canny])

cv.imshow("img_result", img_result)

cv.waitKey(0)
cv.destroyAllWindows()