```python
# Import required libraries
import os
import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConfigurationLoader:
    """
    A class to load configuration from a JSON file.

    Attributes:
        config_file_path (str): The path to the configuration file.
    """

    def __init__(self, config_file_path: str):
        """
        Initialize the ConfigurationLoader instance.

        Args:
            config_file_path (str): The path to the configuration file.
        """
        self.config_file_path = config_file_path

    def load_config(self) -> dict:
        """
        Load the configuration from the JSON file.

        Returns:
            dict: The loaded configuration.
        """
        try:
            # Load the configuration from the JSON file
            with open(self.config_file_path, 'r') as config_file:
                config = json.load(config_file)
                logging.info(f"Loaded configuration from {self.config_file_path}")
                return config
        except FileNotFoundError:
            logging.error(f"Configuration file not found at {self.config_file_path}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse configuration file: {e}")
            raise


def get_environment_variables() -> dict:
    """
    Get the environment variables.

    Returns:
        dict: A dictionary containing the environment variables.
    """
    return {key: value for key, value in os.environ.items()}


def get_configuration(config_file_path: str) -> dict:
    """
    Get the configuration from the JSON file.

    Args:
        config_file_path (str): The path to the configuration file.

    Returns:
        dict: The loaded configuration.
    """
    config_loader = ConfigurationLoader(config_file_path)
    return config_loader.load_config()


def main():
    # Define the configuration file path
    config_file_path = 'config.json'

    # Get the environment variables
    environment_variables = get_environment_variables()
    logging.info("Environment variables:")
    for key, value in environment_variables.items():
        logging.info(f"{key}: {value}")

    # Get the configuration
    configuration = get_configuration(config_file_path)
    logging.info("Configuration:")
    for key, value in configuration.items():
        logging.info(f"{key}: {value}")


if __name__ == "__main__":
    main()
```

```json
# config.json
{
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "username",
        "password": "password"
    },
    "api": {
        "endpoint": "https://api.example.com"
    }
}
```