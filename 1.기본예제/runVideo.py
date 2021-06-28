import cv2 as cv

# VideoCapture의 아규먼트로 불러올 동영상 파일 이름을 사용
cap = cv.VideoCapture("D:/opencv-test/1.기본예제/output.avi")

if cap.isOpened() == False:
    print("동영상을 열 수 없습니다.")
    exit(1)

while(True):

    ret, img_frame = cap.read()


    # 동영상 끝까지 재생하면 read함수는 False를 리턴
    if ret == False:
        print("동영상 파일 읽기 완료")
        break
    
    cv.imshow("Color", img_frame)

    # 동영상 재생 속도를 조절하기 위해 waitKey함수의 아규먼트로 25ms 설정
    key = cv.waitKey(25)

    if key == 27:
        break

cap.release()

cv.destroyAllWindows()