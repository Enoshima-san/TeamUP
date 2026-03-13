```python
# Import required modules
import os
import logging
import json
from datetime import datetime
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Config:
    """
    Class to store and manage application configuration.
    
    Attributes:
    ----------
    config_file : str
        Path to the configuration file.
    config : Dict
        Loaded configuration data.
    """

    def __init__(self, config_file: str):
        """
        Initialize the Config class.

        Parameters:
        ----------
        config_file : str
            Path to the configuration file.
        """
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self) -> Dict:
        """
        Load configuration data from the specified file.

        Returns:
        -------
        Dict
            Loaded configuration data.
        """
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error(f"Configuration file '{self.config_file}' not found.")
            return {}
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON in configuration file '{self.config_file}'.")
            return {}

    def save_config(self, config: Dict) -> None:
        """
        Save configuration data to the specified file.

        Parameters:
        ----------
        config : Dict
            Configuration data to save.
        """
        with open(self.config_file, 'w') as file:
            json.dump(config, file, indent=4)

class Logger:
    """
    Class to manage logging functionality.
    """

    def __init__(self):
        """
        Initialize the Logger class.
        """
        self.logger = logging.getLogger(__name__)

    def info(self, message: str) -> None:
        """
        Log an info message.

        Parameters:
        ----------
        message : str
            Message to log.
        """
        self.logger.info(message)

    def error(self, message: str) -> None:
        """
        Log an error message.

        Parameters:
        ----------
        message : str
            Message to log.
        """
        self.logger.error(message)

class DataProcessor:
    """
    Class to process and manipulate data.
    """

    def __init__(self, data: List):
        """
        Initialize the DataProcessor class.

        Parameters:
        ----------
        data : List
            Data to process.
        """
        self.data = data

    def process_data(self) -> List:
        """
        Process the data.

        Returns:
        -------
        List
            Processed data.
        """
        # Perform data processing operations here
        return self.data

def main():
    """
    Main function to execute the application.
    """
    config_file = 'config.json'
    config = Config(config_file)
    logger = Logger()

    # Load configuration data
    config_data = config.config

    # Process data
    data = [1, 2, 3, 4, 5]
    processor = DataProcessor(data)
    processed_data = processor.process_data()

    # Log info message
    logger.info('Data processing completed.')

    # Save configuration data
    config.save_config(config_data)

if __name__ == '__main__':
    main()
```