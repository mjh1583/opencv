import cv2

# 이미지 읽어오기
img_color = cv2.imread("test.jpg", cv2.IMREAD_COLOR)

if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    exit(1)

# 이미지를 띄울 윈도우의 이름
cv2.namedWindow("Color")

# 이미지 보여줌
cv2.imshow("Color", img_color)

# 아무키 입력시 창 종료
cv2.waitKey(0)
cv2.destroyAllWindows()