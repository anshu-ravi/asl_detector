# ASL Alphabet Detector
The ASL Alphabet Detector is a Python-based application designed to detect and recognize American Sign Language (ASL) alphabets using real-time webcam feeds. It leverages a YOLO (You Only Look Once) model for object detection and provides audio feedback for the detected ASL alphabet signs.

## Features
- Real-time ASL alphabet detection using webcam feed.
- Audio feedback for recognized signs.
- Docker containerization for easy deployment and scalability.

## Prerequisites
Before you begin, ensure you have met the following requirements:

- Docker installed on your system.
- A webcam for capturing video input.

## Installation
The ASL Alphabet Detector is containerized using Docker, simplifying the installation and execution process. Follow these steps to get started:

### Docker Installation
1. Clone the repository:
```
git clone https://github.com/anshu-ravi/asl_detector.git
cd asl_detector
```

2. Build the Docker image:
Navigate to the project directory where the Dockerfile is located and run:
```
docker run --rm -it asl_detector
```

### Normal Installation without Docker 
1. Clone the repository and go into the directory 
2. Create a conda environment called asl and activate it 
3. Install all the required python libraries 
4. Run the main.py file

```
git clone https://github.com/anshu-ravi/asl_detector.git
cd asl_detector
conda create --name asl python=3.9
conda activate asl 
pip install -r requirements.txt  
python main.py
```

# Usage
Once the Docker container is running, the ASL Alphabet Detector automatically starts detecting ASL alphabets using your webcam feed. Detected alphabets will be announced using the system's audio output.

Press 'q' to quit the application.


# License
This project is licensed under the MIT License - see the LICENSE file for details.

