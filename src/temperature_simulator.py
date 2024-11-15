import time
import random
from datetime import datetime
import logging

class TemperatureSimulator:
    def __init__(self, min_temp, max_temp, interval, file_path):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.interval = interval
        self.file_path = file_path

    def generate_temperature(self):
        temperature = random.uniform(self.min_temp, self.max_temp)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        logging.info(f"Generated temperature: {temperature:.2f}°C at {timestamp}")
        return {"timestamp": timestamp, "temperature": temperature}

    def run(self):
        logging.info("Starting temperature simulator...")
        while True:
            data = self.generate_temperature()
            with open(self.file_path, "w") as f:
                f.write(f"{data['timestamp']},{data['temperature']:.2f}")
            print(f"Generated - Timestamp: {data['timestamp']}, Temperature: {data['temperature']:.2f}°C")
            time.sleep(self.interval)