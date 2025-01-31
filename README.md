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
git clone https://github.com/xDragoxboi/Heartrate/
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage
1. Record accelerometer data using Phyphox (No gravity)
2. Export data as CSV from Phyphox and save as "Raw Data.csv".
3. Run the detection script:
```bash
python run.py
```


## Example Output
```
Average Heart Rate: BPM
```
![Sample Visualization](images/Output.png)
