# Industrial Quality Inspection using Computer Vision 🏭👁️

An automated visual inspection pipeline designed to detect surface defects and anomalies on industrial production items using Deep Learning.

## 🚀 Features
* **Defect Detection:** Convolutional Neural Networks (CNNs) pipeline ready to identify micro-cracks, scratches, and anomalies.
* **Robust Preprocessing:** OpenCV pipelines (normalization, thresholding, edge filtering) to handle variable factory lighting conditions.
* **Low-Latency API:** Asynchronous REST endpoints built with FastAPI for real-time inference.
* **Cloud-Ready:** Fully containerized with Docker for rapid deployment on edge devices or cloud servers.

## 🛠️ Tech Stack
* **Deep Learning:** TensorFlow / PyTorch
* **Computer Vision:** OpenCV
* **Backend:** Python, FastAPI
* **Deployment:** Docker

## ⚙️ How to Run Locally (Using Docker)
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/industrial-quality-inspection.git
   ```
2. Build the Docker image:
   ```bash
   docker build -t quality-inspection-api .
   ```
3. Run the container:
   ```bash
   docker run -p 8000:8000 quality-inspection-api
   ```
4. Access the interactive API documentation at: `http://localhost:8000/docs`
