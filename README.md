![](https://img.shields.io/badge/Creater-TCT-FFFF00) ![](https://img.shields.io/badge/development-python-006400) ![](https://img.shields.io/badge/Version-3.9.21-blue)

# VideoCapture
VideoCapture/攝影機,拍照,錄影

## 1. OpenCV (cv2)
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

## 2. py Code

Please refer the file as below.

| **Item** | **py** | **功能** |
|----------|--------------|-------------|
| **1** | **VideoCapture.py** | 開啟鏡頭並拍照及存檔 |
| **2** | **ViedoRecorder.py**| 開啟鏡頭並錄製及存檔 |

------

## About Me
Thanks & Best Regards !

蔡承廷

​Senior Engineer of Semiconductor Product/Testing & ​Automation

Email: ​​kp924606@gmail.com

LinkedIn:https://www.linkedin.comin/tsai-cheng-ting/
