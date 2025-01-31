# Heartbeat Detection from Phyphox Accelerometer Data

Detect heartbeats using Z-axis accelerometer data recorded by the Phyphox app.

## Features
- Low-pass filtering for noise reduction
- Peak detection algorithm
- Heart rate calculation (BPM)
- Visualization of raw/filtered data

## Requirements
- Python 3.8+

## Installation
1. Clone the repository:
```bash
git clone https://github.com/xDragoxboi/Heartrate-/
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage
1. Record accelerometer data using Phyphox (Z-axis only recommended)
2. Export data as CSV from Phyphox
3. Run the detection script:
```bash
python heart_rate_detection.py --input path/to/your_data.csv
```


## Example Output
```
Average Heart Rate: 72.54 BPM
```
![Sample Visualization](images/Output.png)
