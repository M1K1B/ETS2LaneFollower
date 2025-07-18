# Lane Tracking with OpenCV on Euro Truck Simulator 2 Footage

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)

This project implements a real-time **lane detection and tracking** system using Python 3 and OpenCV, tested on **Euro Truck Simulator 2** gameplay footage. It mimics ADAS-style (Advanced Driver Assistance Systems) lane visualization and can serve as a prototype for simulated autonomous driving systems or computer vision-based video post-processing.

## 🚛 Demo

<video width="720" controls>
  <source src="https://github.com/M1K1B/ETS2LaneFollower/blob/main/demo-video.mov" type="video/mov">
  Your browser does not support the video tag.
</video>
[https://github.com/M1K1B/ETS2LaneFollower/demo-video.mov](https://github.com/M1K1B/ETS2LaneFollower/demo-video.mov)

## 🛠 Features

- Lane line detection using color thresholding and edge detection
- Real-time visualization overlay on video feed
- Road curvature and lane deviation estimation

## 📦 Dependencies

- Python 3.7+
- OpenCV (`opencv-python`)
- NumPy
- Matplotlib (optional, for visualization/debugging)

Run with:

```bash
python3 main.py
```
