# Install with: pip install streamlit
import streamlit as st
import numpy as np
import time
import random

st.title("Real-Time Health Monitor")
st.subheader("Monitoring Heart Rate in Real Time")

# Placeholder for chart
chart = st.line_chart([])

data = []

# Simulating real-time data stream
for i in range(100):  # simulate 100 readings
    new_heart_rate = random.randint(60, 100)
    data.append(new_heart_rate)
    
    chart.line_chart(data[-30:])  # keep only last 30 points visible
    time.sleep(1)  # 1-second delay to simulate real-time
