import logging
import yaml

def setup_logging(log_config):
    logging.basicConfig(
        filename=log_config['file'],
        level=getattr(logging, log_config['level'].upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging initialized.")
