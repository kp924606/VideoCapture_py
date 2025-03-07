#The following code is based on the "AI Application Development Course" and has been partially modified after further personal research.

from datetime import datetime
from  deepface import DeepFace as DF #從deepface載入DeepFace, # as 縮寫
import cv2

#開啟攝影機,請注意攝影機編號
cap = cv2.VideoCapture(0)
while cap.isOpened():#鏡頭能開啟?
    
    ret, frame = cap.read() #ret=retval(True:正常、False:不正常),frame=image

    frame=cv2.flip(frame,1) #左右翻轉
    
    try: #嘗試
        #     臉部分析      照片            分析項目
        obj = DF.analyze(img_path =frame, actions = ['age', 'gender', 'emotion']) # 'race'
        
        #依序進入臉部清單
        for face in obj:
            #在畫面寫字 年齡性別情緒
            print(face["age"]," years old ","",face["dominant_emotion"]," ", face["dominant_gender"])
            cv2.putText(frame,str(face["age"]) + ',' + face["dominant_gender"] + ',' +face["dominant_emotion"],(face["region"]["x"],face["region"]["y"]),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)
            
            #繪製出偵測人臉的矩形範圍
            cv2.rectangle(frame, (face["region"]["x"], face["region"]["y"]), (face["region"]["x"]+face["region"]["w"], face["region"]["y"]+face["region"]["h"]), ( 0, 255, 0), 4)
            
            #情緒是 Happy
            if(face["dominant_emotion"] == 'happy'):            
                # 獲取當前時間
                now = datetime.now()
                timestamp = now.strftime("%Y%m%d_%H%M%S")
                # 設定檔案名稱
                filename = fr"data\photo_{timestamp}_happy.jpg"
                #儲存照片
                cv2.imwrite(filename , frame)

    except: #例外處理
        print("no Face Found")

    key=cv2.waitKey(1)#0=強制等待、1:等候1ms就跳過

    # 按ESC離開
    if key == 27:
        break
    # 按1拍照存檔
    elif key == 49:
        # 獲取當前時間
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        # 設定檔案名稱
        filename = fr"data\photo_{timestamp}.jpg"
        #儲存照片
        cv2.imwrite(filename , frame)        

    #顯示畫面
    cv2.imshow('deepface',frame)

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()
