# Construction Site Safety Object Detection using YOLOv8

## Overview

This project implements a YOLOv8-based object detection system for monitoring construction site safety. The model detects personal protective equipment (PPE) and safety-related objects in images.

## Features

* Detects Hard Hats
* Detects Safety Vests
* Detects Masks
* Detects Persons
* Detects Vehicles
* Detects Machinery
* Detects Safety Cones

## Technologies Used

* Python
* YOLOv8
* PyTorch
* OpenCV
* Ultralytics

## Dataset

Construction Site Safety Dataset from Kaggle/Roboflow.

## Project Workflow

1. Dataset Collection
2. Data Preparation
3. Model Training using YOLOv8
4. Model Evaluation
5. Object Detection on Test Images

## Results

The trained YOLOv8 model successfully detects PPE equipment and construction-site objects with good accuracy.

## Files

* train.py → Model training script
* predict.py → Prediction script
* data.yaml → Dataset configuration
* requirements.txt → Project dependencies

## Future Improvements

* Real-time webcam detection
* Streamlit web application
* Safety violation alerts
* Video-based detection system
