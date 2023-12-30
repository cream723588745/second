import cv2

from handutils import hand_detect

import numpy as np

import mediapipe as mp

camera=cv2.VideoCapture(0)
handdetect=hand_detect()

#handdetect=mp.solutions.hands.Hands()

while True:
    success,img=camera.read()
    if success:
        r = 1.5
        sizechange= (int(img.shape[1] * r), int(img.shape[0] * r))
        img = cv2.resize(img, sizechange, interpolation=cv2.INTER_AREA)
        print(img.shape)
        '''img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        result=handdetect.process(img_rgb)
        #print(result.multi_hand_landmarks)  #可以删除 用于打印数据
        if result.multi_hand_landmarks:
            for handlms in result.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(img,handlms,mp.solutions.hands.HAND_CONNECTIONS)'''
        img=cv2.flip(img,1)  #视频镜像翻转
        handdetect.process(img)
        position= handdetect.findposition(img)
        print(position)  #打印个点的位置数据，可删
        '''rightfinger=position['Right'].get(8,None)
        if rightfinger:
            cv2.circle(img,(rightfinger[0],rightfinger[1]),10,(100,0,155),cv2.FILLED)'''  #画大圆点

        #handdetect.Rightposition(img)
        '''hands = mp.solutions.hands.Hands()
        result = hands.process(img)
        rightposition = []
        if result.multi_hand_landmarks:
            hand=result.multi_hand_landmarks[0]
            h, w, c = np.shape(img)
            for i in range(21):
                a = hand.landmark[i].x * w
                b = hand.landmark[i].y * h
                rightposition.append([int(a), int(b)])
        print(rightposition)'''
        '''rightposition = np.array(rightposition, dtype=np.int32)
        hullindex = [0, 1, 2, 3, 6, 10, 14, 19, 18, 17, 10]
        hull = cv2.convexHull(rightposition[hullindex,:])
        cv2.polylines(img, [hull], True, (255, 0, 0), 2)'''


        cv2.imshow('vedio',img)
        k=cv2.waitKey(1)
        if k==ord(' '):
            break
camera.release()
cv2.destroyALLWindows()

