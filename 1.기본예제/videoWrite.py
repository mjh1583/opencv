import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

if cap.isOpened() == False:
    print("카메라를 열 수 없습니다.")
    exit(1)

# 캡처된 이미지의 크기를 확인하기 위해 이미지 1장을 캡처
ret, img_frame = cap.read()

if ret == False:
        print("캡처 실패")
        exit(1)

# 동영상 파일을 위한 코덱을 설정
codec = cv.VideoWriter_fourcc("M", "J", "P", "G")

# 프레임 레이트(Framw rate) 설정
fps = 30.0

# 이미지 크기를 가져옴
h, w = img_frame.shape[:2]

# 동영상 파일을 저장하려면 VideoWriter 객체를 생성해야 함
# VideoWriter 객체를 초기화하기 위해 저장할 동영상 파일 이름, 코덱, 프레임 레이트, 이미지 크기 지정
writer = cv.VideoWriter("D:/opencv-test/1.기본예제/output.avi", codec, fps, (w, h))

# VideoWriter 객체를 성공적으로 초기화 했는지 체크
if writer.isOpened() == False:
    print("동영상 파일을 준비할 수 없습니다.")
    exit(1)

# ESC 키를 눌러서 카메라 앱을 종료하면 종료 직전까지 카메라가 찍은 연속 이미지가 동영상으로 저장됨
while(True):

    # 카메라에서 이미지를 읽어옴
    ret, img_frame = cap.read()

    if ret == False:
        print("캡처 실패")
        exit(1)
    
    # 캡처한 이미지를 동영상 파일에 추가
    writer.write(img_frame)

    cv.imshow("Color", img_frame)

    key = cv.waitKey(1)

    if key == 27:
        break

cap.release()

# 동영상 저장을 완료하기 위해 VideoWriter 객체 릴리즈
writer.release()

cv.destroyAllWindows()