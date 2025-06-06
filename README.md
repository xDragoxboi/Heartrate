# Heartbeat Detection from Phyphox Accelerometer Data
[![Try Now](https://img.shields.io/badge/Try%20Now-Browser%20Version-blue?style=for-the-badge)](https://xdragoxboi.github.io/Heartrate/)

## Note and Info
The live browser version has been significantly updated! It now features improved processing (low-pass filtering and dynamic threshold detection) directly in your browser for better accuracy. While browser sensor polling rates can still be a factor, the detection logic is much more robust. It's also now a single, self-contained HTML file!

Detect heartbeats using Z-axis accelerometer data recorded by the Phyphox app.

## Features
- Low-pass filtering for noise reduction
- Peak detection algorithm
- Heart rate calculation (BPM)
- Visualization of raw/filtered data
*Many of these features, including advanced filtering and peak detection, are now also implemented in the live browser version!*

## Requirements
- Python 3.8+
- Working Heart ( Minimum BPM of NOT DEAD )

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



## Why This Repo Exists (A Dramatic Retelling)

In a world... *where GitHub repos grow to unreasonable sizes*... **one developer dared to ask**:  
*"What if I made a thing that does a tiny thing and put it on the internet anyway?"*  

This project is the answer to questions nobody asked, including:  
- Can a phone detect your heartbeat? *(Sort of!)*  
- Should it? *(Absolutely not!)*  
- Does this code secretly judge your life choices? *(Yes, but politely.)*  

### Motivations Include:
- **Science**: To prove that "good enough" is the enemy of "perfect" (and also sleep).  
- **Art**: To create a plot that looks like a seismograph of your existential crises.  
- **Philosophy**: If a heartbeat is detected in a GitHub repo and nobody stars it, does it make a sound?  

### Why You Should Care
- It’s 10% signal processing, 90% vibes  
- You can tell your parents you’re "doing medical stuff with code"  
- Future archaeologists will find this and think we worshipped hotdogs *(we do)*  

---

**Disclaimer**:  
This project pairs well with:  
- Questioning why you’re reading this README  
- Regretting your life choices  
- Pretending you’re a cyborg when the peaks align  

*Made with ❤️ (and questionable life decisions) by a human who probably needs a hobby.*  
