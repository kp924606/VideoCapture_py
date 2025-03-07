#The following code is based on the "AI Application Development Course" and has been partially modified after further personal research.

import cv2
import dlib #臉部辨識工具
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 120) #語速 50~500
engine.setProperty('volume', 1) #聲音大小 0~1
voices = engine.getProperty('voices')

#選擇第一隻攝影機
cap = cv2.VideoCapture(0)

#取得預設的臉部偵測器
detector = dlib.get_frontal_face_detector()

#根據shape_predictor方法載入68個特徵點模型，此方法為人臉表情識別的偵測器
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat') #注意路徑

#當攝影機打開時，對每個frame進行偵測
while(cap.isOpened()):
    #讀出frame資訊
    ret, frame = cap.read()    
    frame=cv2.resize(frame,(640,480)) #變更解析度
    frame=cv2.flip(frame,1) #左右翻轉
    #偵測人臉
    #人臉座標   人臉評估值 方向
    face_rects, scores, idx = detector.run(frame) 
    #取出偵測的結果 enumerate(列舉)
    for i,face in enumerate(face_rects):
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        # %格式化數字 f=小數點   d=整數decimal
        text = " %2.2f ( %d )" % (scores[i], idx[i])

        #繪製出偵測人臉的矩形範圍
        #繪製矩形      照片    左上      右下      顏色(B,G,R)  線寬
        cv2.rectangle(frame, (x1, y1), (x2, y2), ( 0, 255, 0), 4)

        #標上人臉偵測分數與人臉方向子偵測器編號
        #   寫字     影像   文字    座標      字型                    大小     顏色         粗細
        cv2.putText(frame, text, (x1, y1), cv2. FONT_HERSHEY_DUPLEX, 0.7, ( 255, 255, 255), 1)

        #找出特徵點位置
        shape = predictor(frame, face)
   
        #繪製68個特徵點
        for i in range(68):
            #畫圈      找片     座標                            半徑 顏色(BGR)   線寬
            cv2.circle(frame,(shape.part(i).x,shape.part(i).y), 3,( 0, 0, 255), 2)
            cv2.putText(frame, str(i),(shape.part(i).x,shape.part(i).y),cv2. FONT_HERSHEY_COMPLEX, 0.5,( 255, 0, 0), 1)
       
        #計算嘴巴打開的大小
        open = shape.part(66).y - shape.part(62).y
        print("嘴巴已打開:",open)
        if open > 20:
            print("上課期間，不要講話")
            engine.say("上課期間，不要講話")
            engine.runAndWait()
            
    #輸出到畫面   
    cv2.imshow( "Face Detection", frame)

    #如果按下q键，就退出
    k = cv2.waitKey(1)
    if k == 27:
        break





