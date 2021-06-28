import cv2 as cv

img_gray = cv.imread("D:/opencv-test/2.영상처리기본개념/test.jpg", cv.IMREAD_GRAYSCALE)

# copy 메소드를 사용하여 img_gray의 이미지 데이터를 복사
img_copyed1 = img_gray.copy()

# copy 메소드를 사용했기 때문에 img_gray와 img_copyed1에 대한
# id 리턴값이 다름, 별개의 객체라는 의미
print(id(img_gray), id(img_copyed1))

cv.line(img_gray, (0, 0), (100, 100), 0, 10)

ret, img_gray = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

print(id(img_gray), id(img_copyed1))

cv.imshow("img_gray", img_gray)
cv.imshow("img_copyed1", img_copyed1)

cv.waitKey(0)