# 🚦 AI Based Traffic Management System 🚦

## About the Project

## Aim

The goal of this project is to develop a smart AI-based solution for traffic management on routes with heavy traffic from different directions, incorporating real-time monitoring and adaptive traffic light timing.

## 🌟 Abstract

Urban intersections in India are notorious for traffic congestion, causing endless delays and inefficiencies. Our project introduces NexSpy, an innovative AI model designed to revolutionize traffic light management and significantly reduce congestion. By leveraging cutting-edge computer vision techniques and regression analysis, our solution is both scalable and cost-effective. Seamlessly integrating with existing traffic light infrastructure, our model requires minimal computational resources, making it a practical tool for enhancing traffic flow and reducing delays.

## 🚀 Solution

Our AI model tackles intersection congestion through a sophisticated multi-step process:

Data Collection: Cameras capture video footage at various times of the day and night, which is then processed into a sequence of images at 20 frames per minute.
Image Processing: These images are converted to grayscale, and the density of Canny edges is analyzed to distinguish between empty and congested roads. The area occupied by these edges is quantified and normalized to estimate vehicle count accurately.
Semantic Segmentation: To improve vehicle detection and differentiate between vehicles and non-vehicular objects (like trees and pedestrians), we employ advanced semantic segmentation techniques.
Model Training: Initially trained using reinforcement learning in a Pygame simulation environment, our model is fine-tuned with real-world data for optimal performance.
Traffic Light Management: The AI model predicts traffic patterns and dynamically manages traffic lights to reduce congestion effectively.

## 🛠️ Technologies Used

Computer Vision: Processes video data and detects vehicles using Canny edge detection and semantic segmentation techniques.
Regression Analysis: Estimates vehicle counts and predicts traffic flow patterns.
Pygame Simulation Environment: Facilitates initial training and fine-tuning of the regression model before real-world deployment.
Reinforcement Learning: Optimizes traffic light timings dynamically by learning from real-time traffic data and feedback, improving decision-making and adaptation to changing traffic conditions.

## 🌍 Impact of the Project

Our AI model represents a significant leap forward in traffic management technology, with several key benefits:

Enhanced Traffic Flow: Optimizes traffic light management to reduce delays and improve overall traffic flow at congested intersections.
Cost-Effective Integration: Designed to integrate seamlessly with existing traffic light infrastructure, making it a practical solution for cities with limited budgets.
Scalability: Minimal computational demands and compatibility with existing systems make it a scalable solution for various urban settings.
Reduced Congestion: Decreases travel time and vehicle emissions, contributing to a more efficient and environmentally friendly urban transportation system.
Decreased Pollution: Reduces vehicle idling and improves traffic flow, lowering emissions and contributing to better air quality and a healthier urban environment.
Overall, our AI-driven approach promises to address the pressing issue of traffic congestion in Indian cities, offering a scalable and effective solution to enhance urban mobility.

## Tech Stack

- [SUMO](https://sumo.dlr.de/docs/index.html)
- [Tensorflow](https://www.tensorflow.org/)
- [Python](https://www.python.org/)
- [Matplotlib](https://matplotlib.org/)
- [Numpy](https://numpy.org/doc/#)
- [Google Collab](https://colab.research.google.com/)

## File Structure

    ├── docs
       ├── SIH2024.pdf
       ├── SIH2024.pptx
    ├── files
       ├── Edge Detection.ipynb
       ├── Semantic Segmentation.ipynb
       ├── Semantic Segmentation Module.ipynb
       ├── Sequence of Images.ipynb
    ├── Images
       ├── 01
       ├── 02
       ├── 03
       ├── 04
       ├── 05
       ├── 06
       ├── 07
       ├── 08
       ├── 09
       ├── 10
       ├── 11
       ├── 12
       ├── 13
    ├── main.py
    ├── README.md
    ├── yolo.py
    ├── yolov8n.pt

## Getting Started

## Running the model

1. Clone or download the repository.
2. Using the Anaconda prompt or any other terminal, navigate to the root folder and run the file **main.py** by executing:

```
python main.py
```

## Project Demo

<video width="320" height="240" controls>
  <source src="https://github.com/user-attachments/assets/badfd777-e3c7-4a58-a70e-1aa88833a1ca" type="video/mp4">
  Your browser does not support the video tag.
</video>
<!-- ![Demo Video](https://github.com/user-attachments/assets/badfd777-e3c7-4a58-a70e-1aa88833a1ca) -->

## Contributors

- Abhishek Kotwani
- Aryan Yadav
- Aman Vatsa
- Dhriti A.
- Om Mukherjee
- Ronit Choube
