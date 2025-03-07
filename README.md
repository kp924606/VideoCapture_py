![](https://img.shields.io/badge/Creater-TCT-FFFF00) ![](https://img.shields.io/badge/development-python-006400) ![](https://img.shields.io/badge/Version-3.9.21-blue)

# VideoCapture
VideoCapture/攝影機,拍照,錄影

# 1. Package Introduce

## 1-1. OpenCV (cv2)
（Open Source Computer Vision Library）是一個開源的計算機視覺和機器學習軟件庫，旨在提供各種視覺任務的高效解決方案。它被廣泛應用於影像處理、物體檢測、影像分類、面部識別、計算機視覺等領域。

主要功能：

- 基本處理：旋轉、縮放、裁剪、平移、翻轉、顏色空間轉換（例如：BGR ↔ RGB、灰階、HSV 等）。

- 濾波：使用濾波器（如高斯濾波、邊緣檢測濾波等）來進行降噪或邊緣檢測。

- 圖像增強：調整對比度、亮度、色調，進行直方圖均衡化等。


### 物體檢測與追蹤：

- Haar 特徵分類器：用於面部識別、人臉檢測。

- HOG（Histogram of Oriented Gradients）：用於人類檢測。

- SSD（Single Shot Multibox Detector）/YOLO（You Only Look Once）：用於實時物體檢測。

- 物體追蹤：追蹤目標物體，例如使用 Meanshift 和 Camshift 進行物體跟踪。

### 特徵檢測與匹配：

- 角點檢測：如 Harris 角點檢測。
- SIFT/SURF：尺度不變特徵轉換，用於特徵檢測和匹配。
- ORB（Oriented FAST and Rotated BRIEF）：用於更快的特徵匹配。

- 機器學習：
支持向量機（SVM）：用於分類。
神經網絡：OpenCV 提供了深度學習的接口，可以使用預訓練的模型，如 Caffe、TensorFlow 等。

- 視頻處理：
讀取視頻：通過 cv2.VideoCapture 讀取攝像頭或視頻檔案。

  視頻錄製：用 cv2.VideoWriter 寫入視頻，支援多種格式（如 .avi、.mp4）。
  
  包括解析度調整、幀率修改、視頻剪輯等。

- 圖像變換：
透視變換：進行視角變換、圖像扭曲。

  圖像分割：將圖像劃分為多個區域。

- 計算機視覺任務：
文字識別（OCR）：透過 tesseract 等工具進行文本識別。

  手勢識別、人臉識別、姿態估計 等。

- 跨平台：
支援多種操作系統，如 Windows、Linux、macOS，並提供多種語言接口，最常用的是 C++ 和 Python，但也有 Java 和其他語言支持。

與硬體的兼容性好：支援多種影像擷取裝置，包括 WebCAM、USB 攝像頭、專業相機等，並能高效處理來自不同來源的視頻流。

易於集成與擴展：易於與其他機器學習庫（如 TensorFlow、PyTorch）集成，也能與硬體設備、網路接口等進行整合。

------
## 1-2. DeepFace
DeepFace 是 Python 的人臉辨識與分析套件，基於 深度學習，支援多種人臉辨識模型。
提供了 人臉比對、人臉分析（年齡、性別、情緒）、特徵嵌入（Embeddings）等功能，並且相對簡單易用。

主要功能：
| **Item** | **功能** |
|----------|--------------|
| **1** | 人臉辨識（Face Recognition）	比較兩張人臉是否為同一人 |
| **2** | 人臉驗證（Face Verification）	驗證人臉與特定身份是否匹配 |
| **3** | 人臉特徵擷取（Embeddings）	產生可比較的人臉特徵向量 |
| **4** | 年齡預測（Age Estimation）	預測人臉的年齡 |
| **5** | 性別預測（Gender Prediction）	預測性別（Male / Female）|
| **6** | 情緒偵測（Emotion Detection）	偵測表情，如快樂、悲傷、驚訝等 |
| **7** | 人臉對齊（Face Alignment）	將人臉調整至標準方向，提升辨識率 |

### 優點:
- ✅ 支援多種預訓練模型：
VGG-Face、Google FaceNet、OpenFace、DeepID、ArcFace、Dlib、SFace

- ✅ 準確度高：
基於 深度學習，比傳統人臉偵測方法（如 OpenCV）更精確

- ✅ 開箱即用：
API 設計簡單，幾行程式就能完成人臉辨識或分析

- ✅ 支援 GPU 加速：
若安裝 TensorFlow 或 PyTorch，可利用 CUDA 加速計算

- ✅ 多種影像格式支援：
可處理 PNG、JPG、BMP 等格式，也可直接分析 影片與攝影機畫面

------
## 1-3. dlib
dlib 是一個強大的機器學習庫，主要用於人臉識別、物體檢測、圖像處理和其他與計算機視覺有關的任務。它提供了多種功能來進行物體偵測、人臉識別、特徵點檢測等任務。

### 優點:
- ✅ 高效準確：
dlib 提供的臉部偵測和特徵點檢測工具，能夠在大多數情況下進行高效且準確的偵測。

- ✅ 簡單易用：
提供簡單的 API，使得開發者能夠快速進行人臉檢測和特徵點提取。
  
- ✅ 跨平台支持：
dlib 可在多種操作系統（如 Windows、Linux、macOS）上運行。

- ✅ 開源：
dlib 是一個開源庫，這意味著它可以免費使用並且可修改。

------
## 2. py Code

Please refer the file as below.

| **Item** | **py** | **功能** |
|----------|--------------|-------------|
| **1** | **VideoCapture.py** | 開啟鏡頭並拍照及存檔 |
| **2** | **ViedoRecorder.py**| 開啟鏡頭並錄製及存檔 |
| **3** | **VideoCapture_FaceGenderAge.py**| 開啟鏡頭並分析臉部性別年齡(DeepFace) |
| **4** | **VideoCapture_FaceCoordinates1.py**| 開啟鏡頭並分析人臉68個特徵點模型(dlib) |

------

## 3. py Sample Result

- VideoCapture_FaceGenderAge.py
  Show Human age, Gender.
  
![image](https://github.com/user-attachments/assets/fbdc20db-c70b-4f0e-9614-b113239c848b)

- VideoCapture_FaceCoordinates1.py
  Draw 68 points on the model's face.
  
  ![image](https://github.com/user-attachments/assets/4b6e1db6-8824-4b46-a991-68aa7a1b11c6)

  Please refer the Sample as below.
  
  ![image](https://github.com/user-attachments/assets/d3af697f-ce12-44ee-926f-6c8a8b630d66)

  ![image](https://github.com/user-attachments/assets/4f53534c-4b97-4326-ab46-0af8c69777c1)

  You can determine the distance between the 68 points drawn on the model's face based on the expression.
  For example: Determine if the person is speaking based on the distance between two points(62 & 66) on the mouth.
  
  ![image](https://github.com/user-attachments/assets/30157267-d5e7-4d6c-9921-fae33d717a61)


------

## About Me
Thanks & Best Regards !

蔡承廷

​Senior Engineer of Semiconductor Product/Testing & ​Automation

Email: ​​kp924606@gmail.com

LinkedIn:https://www.linkedin.comin/tsai-cheng-ting/
