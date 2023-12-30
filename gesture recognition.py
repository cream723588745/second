import mediapipe as mp
import cv2
import numpy as np


# 定义获取指关节角度的函数
def get_angle(v1, v2):
    angle = np.dot(v1, v2) / (np.sqrt(np.sum(v1 * v1)) * np.sqrt(np.sum(v2 * v2)))
    angle = np.arccos(angle) / 3.14 * 180
    return angle


# 定义获取手势的函数
def get_str_guester(up_fingers, list_point):
    if len(up_fingers) == 1 and up_fingers[0] == 8:  # 当只有手指8竖起时
        v1 = list_point[6] - list_point[7]
        v2 = list_point[8] - list_point[7]
        # 通过判断两个关节的角度来判断该手指是否是弯曲的
        angle = get_angle(v1, v2)
        if angle < 160:
            str_guester = "9"
        else:
            str_guester = "1"
    elif len(up_fingers) == 1 and up_fingers[0] == 4:
        str_guester = "Good"
    elif len(up_fingers) == 1 and up_fingers[0] == 20:
        str_guester = "Bad"
    elif len(up_fingers) == 2 and up_fingers[0] == 8 and up_fingers[1] == 12:
        str_guester = "2"
    elif len(up_fingers) == 2 and up_fingers[0] == 4 and up_fingers[1] == 20:
        str_guester = "6"
    elif len(up_fingers) == 2 and up_fingers[0] == 4 and up_fingers[1] == 8:
        str_guester = "8"
    elif len(up_fingers) == 3 and up_fingers[0] == 8 and up_fingers[1] == 12 and up_fingers[2] == 16:
        str_guester = "3"
    elif len(up_fingers) == 3 and up_fingers[0] == 4 and up_fingers[1] == 8 and up_fingers[2] == 12:
        str_guester = "7"
    elif len(up_fingers) == 3 and up_fingers[0] == 4 and up_fingers[1] == 8 and up_fingers[2] == 20:
        str_guester = "Rock"
    elif len(up_fingers) == 4 and up_fingers[0] == 8 and up_fingers[1] == 12 and up_fingers[2] == 16 and up_fingers[
        3] == 20:
        str_guester = "4"
    elif len(up_fingers) == 5:
        str_guester = "5"
    elif len(up_fingers) == 0:
        str_guester = "10"
    else:
        str_guester = " "
    return str_guester


if __name__ == "__main__":
    cap = cv2.VideoCapture(0);
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    while True:
        success, img = cap.read()  # 读取每一张图片
        if not success:
            continue
        image_height, image_width, imagedepth = np.shape(img)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)  # 将图片带入到函数中处理，得到result
        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]  # 找到第一个手并画出来
            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)
            list_point = []  # 放置关键点的坐标list
            for i in range(21):
                pos_x = hand.landmark[i].x * image_width
                pos_y = hand.landmark[i].y * image_height
                list_point.append([int(pos_x), int(pos_y)])
            # 构造凸包
            list_point = np.array(list_point, dtype=np.int32)
            hull_index = [0, 1, 2, 3, 6, 10, 14, 19, 18, 17, 10]
            hull = cv2.convexHull(list_point[hull_index, :])
            cv2.polylines(img, [hull], True, (0, 255, 0), 2)  # 绘制凸包
            print(list_point)
            # 查找哪些手指指尖在手掌外
            n_fig = -1
            obj_finger = [4, 8, 12, 16, 20]
            up_fingers = []  # 存放结果
            for i in obj_finger:
                pt = (int(list_point[i][0]), int(list_point[i][1]))
                dist = cv2.pointPolygonTest(hull, pt, True)  # 判断这个点是否在凸包里面
                if dist < 0:
                    up_fingers.append(i)
            # 根据得到的手指判断
            # 手势
            str_guester = get_str_guester(up_fingers, list_point)
            cv2.putText(img, '%s' % (str_guester), (90, 90), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 0), 4,
                        cv2.LINE_AA)  # 在视频中显示出来判断的手势
            # for i in obj_finger:
            # pos_x=hand.landmark[i].x*image_width
            # pos_y=hand.landmark[i].y*image_height
            # cv2.circle(img,(int(pos_x,pos_y)),3,(0,255,255),-1)
        cv2.imshow("hand", img)  # 显示结果
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    cap.release()