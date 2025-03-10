AI-powered mood detection using **OpenCV**, **MediaPipe**, and **DeepFace**. This project captures real-time video from your webcam, detects faces, and analyzes emotions.

---

## 📌 Features
```
✅ Real-time Face Detection using MediaPipe  
✅ Emotion Recognition using DeepFace  
✅ Live Mood Display on Video Feed  
✅ Press 'Q' to Quit  
```

---

## 🚀 Installation & Setup

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/vighneshwar/ai-mood-detector.git
cd ai-mood-detector
```

### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ **Install Dependencies**
```sh
pip install opencv-python mediapipe deepface pyttsx3
```

### 4️⃣ **Run the Mood Detector**
```sh
python mood_detector.py
```

---

## 🖥️ How It Works
```
1. Captures real-time video using OpenCV.  
2. Detects faces using MediaPipe.  
3. Extracts facial ROI and analyzes dominant emotion with DeepFace.  
4. Displays detected mood on the video feed.  
```

---

## 🖼️ Demo Screenshot
```
(Upload a screenshot and replace 'demo_screenshot.png')
![Mood Detector in Action](demo_screenshot.png)
```

---

## 🛠 Troubleshooting
```
🔹 Camera Not Opening? → Check if another app is using the webcam.  
🔹 Mood Not Detected? → Ensure DeepFace is installed and working properly.  
🔹 Slow Performance? → Run on a system with a dedicated GPU for better speed.  
```

---

## 📝 License
```
This project is open-source under the MIT License.
```

---

## 🤝 Contributions
```
💡 Contributions Welcome! Feel free to fork, improve, and submit PRs.  
📩 Got Issues? Open an issue at https://github.com/vighneshwarkuru/ai-mood-detector/issues  
🚀 Happy Coding! 😃  
```

---