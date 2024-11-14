import time
import logging

class TemperatureClient:
    def __init__(self, file_path, poll_interval):
        self.file_path = file_path
        self.poll_interval = poll_interval
        self.last_timestamp = None

    def check_for_new_data(self):
        try:
            with open(self.file_path, "r") as f:
                line = f.readline().strip()
                timestamp, temperature = line.split(",")
                if timestamp != self.last_timestamp:
                    self.last_timestamp = timestamp
                    logging.info(f"New data - Timestamp: {timestamp}, Temperature: {temperature}°C")
                    print(f"New temperature data - Timestamp: {timestamp}, Temperature: {temperature}°C")
        except FileNotFoundError:
            logging.error("Data file not found.")
        except Exception as e:
            logging.error(f"Error reading data: {e}")

    def run(self):
        logging.info("Starting client polling...")
        while True:
            self.check_for_new_data()
            time.sleep(self.poll_interval)
