# virtual_volume-controle
🖐️ Hand Gesture Volume Control using OpenCV & MediaPipe

This project allows you to control your system volume using hand gestures in real-time.
By detecting hand landmarks, the distance between thumb and index finger is used to increase or decrease the system volume — just like a smart gesture interface 🎚️🤖

🚀 Features

Real-time hand tracking using MediaPipe

Volume control using thumb–index finger distance

Smooth volume scaling

FPS display for performance

Works with any webcam

🛠️ Technologies Used

Python

OpenCV

MediaPipe

PyCaw (for audio control on Windows)

NumPy

📂 Folder Structure
└── HandVolumeControl
    ├── volume_control.py
    ├── requirements.txt
    └── README.md

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/rabia-akrm/virtual_volume-controle.git
cd virtual_volume-controle

2️⃣ Install required libraries
pip install opencv-python mediapipe numpy comtypes pycaw

▶️ Run the Program
python volume_control.py
