#The following code is based on the "AI Application Development Course" and has been partially modified after further personal research.

import cv2 #引入電腦視覺cv2
from datetime import datetime
cap = cv2.VideoCapture(0) #影像擷取裝置，數字:監視器、文字:影片或網址

# 獲取裝置的最大解析度
max_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
max_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 設定為裝置的最大解析度
cap.set(cv2.CAP_PROP_FRAME_WIDTH, max_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, max_height)

while cap.isOpened():
  ret, frame = cap.read() #ret=retval(True:正常、False:不正常),frame=image    
  cv2.imshow('frame', frame)
  
  key=cv2.waitKey(1)#等候使用者按鍵盤1ms
  #print("key:",key)

  #key = chr(cv2.waitKey(1) & 0xFF)  # 等候使用者按鍵盤1ms,將鍵盤按鍵的 ASCII 值轉換為字符  
 
  if key == 27: #使用者按了鍵盤'ESC'
    break #退出while
  elif key == 80 or key == 112:
    #按下p
    # 獲取當前時間
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    # 設定檔案名稱
    filename = f"image\photo_{timestamp}.jpg"

    #儲存檔案
    cv2.imwrite(filename , frame)
    
print("完成")