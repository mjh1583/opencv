import cv2 as cv

# 카메라에서 이미지를 캡처하기 위해서는 VideoCapture 객체를 생성하여 카메라와 연결
# 카메라 인덱스를 아규먼트로 사용
# PC에 처음 연결한 카메라의 인덱스는 0
# 2번째로 연결한 카메라의 인덱스는 1
# PC에 카메라를 연결한 순서에 맞추어 카메라에 접근할 때 사용하는 인덱스 부여
# 카메라에서 캡처를 중지하면 경고 메세지가 나타나는데 두 번째 아규먼트에 cv.CAP_DSHOW를 지정하면 해결됨
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

# 카메라와 성공적으로 연결되었는지 체크
if cap.isOpened() == False:
    print("카메라를 열 수 없습니다.")
    exit(1)

# 카메라에서 이미지 캡처와 윈도우에 이미지 보여주는 것을 반복하면 동영상처럼 보임
while(True):

    # 카메라에서 이미지를 읽어옴
    ret, img_frame = cap.read()

    # ret 리턴값이 False이면 캡처 실패
    if ret == False:
        print("캡처 실패")
        exit(1)
    
    # 캡처한 이미지를 윈도우에 보여줌
    cv.imshow("Color", img_frame)

    # 사용자의 키보드 입력을 1ms 동안 기다렸다가 다음 코드 실행
    key = cv.waitKey(1)

    # ESC 키가 입력되었다면 반복을 중지
    if key == 27:
        break

# 사용이 끝난 카메라와 연결 종료
cap.release()
cv.destroyAllWindows()