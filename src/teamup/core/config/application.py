```python
from pydantic import BaseSettings, SettingsConfigDict

class ApplicationSettings(BaseSettings):
    """
    Application settings class.

    This class represents the application settings, including name, environment,
    debug mode, host, and port.
    """

    # Application name
    app_name: str

    # Environment (e.g., development, production)
    environment: str

    # Debug mode
    debug_mode: bool

    # Host IP address
    host_ip: str

    # Host port
    port_number: int

    class Config:
        """
        Configuration settings for the ApplicationSettings class.
        """

        # Environment prefix for settings
        env_prefix = "APP_"

        # Path to the environment file
        env_file = ".env"

        # Encoding for the environment file
        env_file_encoding = "utf-8"

        # Extra settings behavior
        extra = "ignore"

    def is_debug_mode(self) -> bool:
        """
        Returns the debug mode setting.

        Args:
            None

        Returns:
            bool: The debug mode setting.
        """
        return self.debug_mode
```