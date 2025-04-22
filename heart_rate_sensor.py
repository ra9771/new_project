import random
import time

def get_heart_rate():
    # Simulate heart rate between 60-100 bpm
    return random.randint(60, 100)

# For testing
if __name__ == "__main__":
    while True:
        print("Heart Rate:", get_heart_rate())
        time.sleep(2)
