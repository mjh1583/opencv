import cv2 as cv
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

if cap.isOpened() == False:
    print("카메라를 열 수 없습니다.")
    sys.exit(1)

# 보여줄 결과를 지정하기 위해 사용하는 변수
step = 1

while(True):

    # img_frame 변수에 대입된 이미지를 윈도우에 보여줌
    # 처음에는 카메라에서 캡처된 컬러 이미지
    ret, img_frame = cap.read()

    if ret == False:
        print("캡처 실패")
        break

    # step이 2이상이면 img_frame에는 그레이 스케일 이미지 대입
    if step > 1:
        img_frame = cv.cvtColor(img_frame, cv.COLOR_BGR2GRAY)

        # step이 3이상이면 img_frame에는 에지 이미지 대입
        if step > 2:
            img_frame = cv.Canny(img_frame, 30, 90)
    
    # 앞에서 처리된 결과에 따라 다른 이미지가 Result 윈도우에 보여짐
    cv.imshow("Result", img_frame)

    # 1초 동안 키보드 입력 대기
    key = cv.waitKey(1)

    # ESC
    if key == 27: 
        break

    # 입력된 키에 따라 step 변수에 다른 값 대입
    # python에서는 ord 함수를 사용하여 문자를 ASCII 코드로 변환 가능
    elif key == ord("1"):
        step = 1
    elif key == ord("2"):
        step = 2
    elif key == ord("3"):
        step = 3

cap.release()
cv.destroyAllWindows()