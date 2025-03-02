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

fps = 60  # 幀率（你可以根據需要調整）

# 定義 VideoWriter，這會將影片儲存為 avi 格式
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 使用 XVID 編碼器

# 獲取當前時間
now = datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M%S")

# 設定檔案名稱
filename = fr"video\video_{timestamp}.avi"

out = cv2.VideoWriter(filename, fourcc, fps, (max_width, max_height))

while True:
    ret, frame = cap.read()  # 捕獲每一幀
    if not ret:
        break
    
    # 寫入影片檔案
    out.write(frame)
    
    # 顯示畫面
    cv2.imshow("Recording", frame)
    
    # 按 'q' 鍵結束錄製
    if cv2.waitKey(1) == 27:
        break

# 釋放資源
cap.release()
out.release()
cv2.destroyAllWindows()
  
print("完成")