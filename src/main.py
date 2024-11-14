import threading
import yaml
from logs.logger import setup_logging
from temperature_simulator import TemperatureSimulator
from temperature_client import TemperatureClient

def load_config(config_file="config.yaml"):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config()
    setup_logging(config['logging'])

    # Creating Client and Simulator with the config. parameters
    simulator = TemperatureSimulator(
        min_temp=config['temperature_simulator']['min_temp'],
        max_temp=config['temperature_simulator']['max_temp'],
        interval=config['temperature_simulator']['interval'],
        file_path=config['temperature_simulator']['file_path']
    )

    client = TemperatureClient(
        file_path=config['temperature_simulator']['file_path'],
        poll_interval=config['temperature_client']['poll_interval']
    )

    # Executing them as separate threads
    
    simulator_thread = threading.Thread(target=simulator.run)
    client_thread = threading.Thread(target=client.run)

    simulator_thread.start()
    client_thread.start()

    simulator_thread.join()
    client_thread.join()

if __name__ == "__main__":
    main()
