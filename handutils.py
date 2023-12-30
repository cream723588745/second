import mediapipe as mp

import cv2

import numpy as np

import pynput

control= pynput.mouse.Controller()

class hand_detect():
    def __init__(self):
        self.handdetect = mp.solutions.hands.Hands()
        self.drawer=mp.solutions.drawing_utils

    def findposition(self,img):
        h,w,c=img.shape
        self.position={'Left':{},'Right':{}}
        if self.handsdata.multi_hand_landmarks:
            i=0
            for fingerpoint in self.handsdata.multi_handedness:

                score=fingerpoint.classification[0].score
                if score >=0.8:
                    label=fingerpoint.classification[0].label
                    handlms=self.handsdata.multi_hand_landmarks[i].landmark
                    for id,lm in enumerate(handlms):
                        x,y =int(lm.x*w),int(lm.y*h)
                        self.position[label][id]=(x,y)
                i=i+1
        return self.position

    def process(self,img):
        count=1
        h, w, c = np.shape(img)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.handsdata = self.handdetect.process(img_rgb)
        #print(self.handsdata.multi_hand_landmarks)  #可以删除 用于打印数据  #已废除
        if self.handsdata.multi_hand_landmarks:
            for handlms in self.handsdata.multi_hand_landmarks:
                self.drawer.draw_landmarks(img, handlms, mp.solutions.hands.HAND_CONNECTIONS)
            rightposition = []
            for i in range(21):
                a= handlms.landmark[i].x * w
                b = handlms.landmark[i].y * h
                rightposition.append([int(a), int(b)])
            list = np.array(rightposition, dtype=np.int32)
            tubaopoint = [0, 1, 2, 3, 7, 11, 15, 19, 18, 17, 10]
            hull = cv2.convexHull(list[tubaopoint, :])
            cv2.polylines(img, [hull], True, (100,100,55), 2)
            #print(rightposition) #可以打印个点坐标，与findposition函数打印的坐标相同


            nfing=-1
            outpoint=[4,8,12,16,20]
            upfingers=[]

            for n in outpoint:
                pt=(int(list[n][0]),int(list[n][1]))
                dist=cv2.pointPolygonTest(hull,pt,True)
                if (rightposition[4][1]-rightposition[8][1])<20:
                    control.press(pynput.mouse.Button.left)
                else:
                    control.release(pynput.mouse.Button.left)
                if dist<0:
                    upfingers.append(n)
                    if len(upfingers)==2 and upfingers[0]==4 and upfingers[1]==8:
                        control.position = ((rightposition[0][0] - 300) * 4, (rightposition[0][1] - 450) * 4)







    '''def findposition(self,img):
        h,w,c=img.shape
        self.position={'Left':{},'Right':{}}
        if self.handsdata.multi_hand_landmarks:
            i=0
            for fingerpoint in self.handsdata.multi_handedness:

                score=fingerpoint.classification[0].score
                if score >=0.8:
                    label=fingerpoint.classification[0].label
                    handlms=self.handsdata.multi_hand_landmarks[i].landmark
                    for id,lm in enumerate(handlms):
                        x,y =int(lm.x*w),int(lm.y*h)
                        self.position[label][id]=(x,y)
                i=i+1
        return self.position'''


    '''def Rightposition(self,img):
        h, w, c = img.shape
        rightposition = []
        for i in range(21):
            handlms = self.handsdata.multi_hand_landmarks[i].landmark
            a=handlms.x*w
            b=handlms.y*h
            rightposition.append([int(a),int(b)])
        return rightposition'''

        #rightposition = np.array(self.rightposition, dtype=np.int32)
        #hullindex = [0, 1, 2, 3, 6, 10, 14, 19, 18, 17, 10]
        #hull = cv2.convexHull(self.rightposition[hullindex, :])
        #cv2.polylines(img, [hull], True, (255, 0, 0), 2)



    '''def Rightposition(self,img):
        h, w,c= img.shape
        rightposition = []
        if self.handsdata.multi_hand_landmarks:
            i=0
            for fingerpoint in self.handsdata.multi_handedness:

                score=fingerpoint.classification[0].score
                if score >=0.8:
                    label=fingerpoint.classification[0].label
                    handlms=self.handsdata.multi_hand_landmarks[i].landmark
                    for id,lm in enumerate(handlms):
                        x,y =int(lm.x*w),int(lm.y*h)
                        rightposition.append([x,y])
                i=i+1
        return rightposition
        print(rightposition)

        rightposition=np.array(self.rightposition,dtype=np.int32)
        hullindex=[0,1,2,3,6,10,14,19,18,17,10]
        hull=cv2.convexHull(self.rightposition[hullindex,:])
        cv2.polylines(img,[hull],True,(255,0,0),2)'''













