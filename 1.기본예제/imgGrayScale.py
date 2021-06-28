import cv2

# 컬러 이미지로 파일 읽어옴
img_color = cv2.imread("D:/opencv-test/1.기본예제/test.jpg", cv2.IMREAD_COLOR)

if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    exit(1)

# 컬러 이미지를 먼저 보여줌
cv2.namedWindow("Color")
cv2.imshow("Color", img_color)

# 대기하다가 키보드 입력이 있으면 다음 코드 실행
cv2.waitKey(0)

# img_color에 저장된 컬러 이미지를 그레이 스케일 이미지로 변환 후 img_gray에 대입
# COLOR_BGR2GRAY는 BGR 채널을 가진 컬러 이미지를 그레이 스케일로 변환하겠다고 지정하는 것
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# nameWindow 함수 생략
# img_gray에 저장된 그레이 스케일 이미지를 식별자가 GraySacle인 창에 보여줌
# 첫 번째 아규먼트를 앞에서 컬러 이미지를 보여줄 때 사용한 
# "Color"를 사용하도록 수정하면 그레이 스케일 이미지가 "Color" 창에 나타남
cv2.imshow("GrayScale", img_gray)

# img_gray에 저장된 이미지를 첫 번째 아규먼트로 지정한 파일로 저장
# 이미지 포맷은 지정한 파일의 확장자에 따라 결정
cv2.imwrite("D:/opencv-test/1.기본예제/grayScale.jpg", img_gray)

# 아무 키 입력 시 프로그램 종료
cv2.waitKey(0)
cv2.destroyAllWindows()