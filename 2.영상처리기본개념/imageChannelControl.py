import cv2 as cv

img_color = cv.imread("D:/opencv-test/2.영상처리기본개념/test.jpg", cv.IMREAD_COLOR)

# 컬러 이미지를 채널별로 분리
img_b, img_g, img_r = cv.split(img_color)

# 채널별 이미지를 조합하여 컬러 영상을 생성
img_result = cv.merge((img_b, img_g, img_r))

cv.imshow("img_color", img_color)
cv.imshow("img_b", img_b)
cv.imshow("img_g", img_g)
cv.imshow("img_r", img_r)

cv.waitKey(0)
cv.destroyAllWindows()