from PIL import ImageGrab
import cv2
import keyboard
import numpy as np
import math
import time

# https://return-value.tistory.com/54
class SideCap:
    def __init__(self):
        self.img_src = np.zeros((640, 480, 1), np.uint8)  # tmp 값, 흑백
        self.img_edge = np.zeros((640, 480, 1), np.uint8)  # tmp 값, 흑백
        self.img_result = np.zeros((640, 480, 3), np.uint8)  # tmp 값, 컬러

        # 이진화 변수, 환경에 따라 값이 조금 씩 다르다.
        self.thresh = 200
        self.maxValue = 255

        self.interval = 0
        self.side_coords = (1090, 685, 1340, 940)  # 원화는 좌표로 설정.

    def side_cap(self):
        """
        차로 캡쳐 
        """
        print("캡쳐 시작.")
        while True:
            self.img_src = cv2.cvtColor(np.array(ImageGrab.grab(
                bbox=self.side_coords)), cv2.COLOR_BGR2GRAY)

            self.make_binary()
            self.houghline()
            self.auto_control()

            cv2.imshow("side cap", self.img_src)
            cv2.imshow("result", self.img_result)

            key = cv2.waitKey(100)
            if key == ord('q'):
                print("캡쳐 중단.")
                cv2.destroyAllWindows()
                return

    def make_binary(self):
        """
        canny를 통한 이진화
        """
        ret, self.img_edge = cv2.threshold(self.img_src, self.thresh, self.maxValue,
                                           cv2.THRESH_BINARY)
        self.img_result = cv2.cvtColor(self.img_edge, cv2.COLOR_GRAY2BGR)

    def houghline(self):
        """
        직선 추출 및 간격 계산
        """
        lines = cv2.HoughLinesP(
            self.img_edge, 1, np.pi/180, 90, None, 10, 30)
        if lines is not None:
            for i in range(0, len(lines)):
                l = lines[i][0]
                self.cal_interval(l)
                cv2.line(self.img_result, (l[0], l[1]), (l[2], l[3]),
                         (0, 0, 255), 3, cv2.LINE_AA)
        else:
            self.interval = 0

    def cal_interval(self, lane_coords):
        """
        점과 직선 사이의 거리
         """
        m = round((lane_coords[2]-lane_coords[0]) /
                  (lane_coords[3]-lane_coords[1]), 2)
        print("좌표 0 : {}, {}".format(lane_coords[2], lane_coords[3]))
        print("좌표 1 : {}, {}".format(lane_coords[0], lane_coords[1]))
        print("m : {}".format(m))
        (a, b, c) = (-m, 1, m*lane_coords[1]-lane_coords[0])
        self.interval = round(abs(a*1930+b*930+c)/math.sqrt(a**2+b**2), 2)
        print("간격 : {}".format(self.interval))

    def auto_control(self):
        """
        interval 값을 기준으로 
        차로 유지하는 함수

        좌향 : a, 우향 :d
        """
        # 차로 좌측으로 이탈 중
        if 550 < self.interval < 1500:
            print("차로를 조정합니다.\n",
                  "auto control : ->")
            keyboard.press('D')
            time.sleep(0.008)
            keyboard.release('D')
        # 차로 우측으로 이탈 중
        elif 50 < self.interval < 300:
            print("차로를 조정합니다.\n",
                  "auto control : <-")
            keyboard.press('A')
            time.sleep(0.008)
            keyboard.release('A')
        else:
            pass


side = SideCap()
keyboard.add_hotkey("alt+C", lambda: side.side_cap())

keyboard.wait('esc')
print("프로그램 종료")