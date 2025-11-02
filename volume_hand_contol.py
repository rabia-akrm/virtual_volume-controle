import cv2 
import time
import numpy as np
import math
from cvzone.HandTrackingModule import HandDetector
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

######################
Wcam,Hcam=640,480
######################

cap=cv2.VideoCapture(0)
cap.set(3,Wcam)
cap.set(4,Hcam)
pTime=0
detector=HandDetector(detectionCon=0.7)

##############volume Control Setup##############
devices = AudioUtilities.GetSpeakers()
device = devices

interface = device.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol=0
volBar=400
volPer=0

while True:
    success,img = cap.read()

    hands, img = detector.findHands(img)  
    lmList = hands[0]['lmList'] if hands else []  

    if len(lmList) != 0:
        x1,y1 = lmList[4][0], lmList[4][1] 
        x2,y2 = lmList[8][0], lmList[8][1] 
        cx,cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)
        print(length)

        vol = np.interp(length, [30,180], [0, 1])
        volume.SetMasterVolumeLevelScalar(vol, None)

        volBar = np.interp(length, [30,180], [400, 150])
        volPer = np.interp(length, [30,180], [0, 100])

        print(int(length), vol)

        if length < 50:
            cv2.circle(img,(cx,cy),15,(0,255,0),cv2.FILLED)

    cv2.rectangle(img, (50,150), (85,400), (255,0,0),3)
    cv2.rectangle(img, (50,int(volBar)), (85,400), (255,0,0),cv2.FILLED)
    cv2.putText(img, f'{int(volPer)}%', (40,450), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 3)   

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (40,50), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 3)   

    cv2.imshow("Image", img)
    cv2.waitKey(1)
