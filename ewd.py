import cv2
import numpy as np
import time
from threading import Thread

class EarlyWarningDevice:
    def __init__(self):
        self.drowsiness_threshold = 0.25  # EAR threshold
        self.obstacle_limit = 50          # Distance in cm
        self.is_active = True
        
    def detect_drowsiness(self):
        """Simulates eye monitoring using OpenCV facial landmarks."""
        cap = cv2.VideoCapture(0)
        while self.is_active:
            ret, frame = cap.read()
            # Placeholder for EAR calculation logic using dlib or Mediapipe
            # If EAR < self.drowsiness_threshold for 2.0s:
            #     print("ALERT: Drowsiness Detected!")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()

    def monitor_obstacles(self):
        """Simulates distance monitoring from an ultrasonic sensor."""
        while self.is_active:
            # Simulated distance from sensor
            dist = np.random.randint(10, 200)
            if dist < self.obstacle_limit:
                print(f"CRITICAL: Obstacle at {dist}cm! Braking suggested.")
            time.sleep(0.5)

    def run(self):
        print("EWD System Initialized...")
        t1 = Thread(target=self.detect_drowsiness)
        t2 = Thread(target=self.monitor_obstacles)
        t1.start()
        t2.start()

if __name__ == "__main__":
    ewd = EarlyWarningDevice()
    ewd.run()
