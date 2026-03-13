```python
from pydantic import BaseSettings, SettingsConfigDict

class SecuritySettings(BaseSettings):
    """
    Security settings for the application.

    Attributes:
    - algorithm (str): The encryption algorithm used.
    - secret_key (str): The secret key used for encryption.
    - access_token_expires_minutes (int): The expiration time for access tokens in minutes.
    - refresh_token_expires_days (int): The expiration time for refresh tokens in days.
    """

    algorithm: str = Field(..., description="Encryption algorithm used")
    secret_key: str = Field(..., description="Secret key used for encryption")
    access_token_expires_minutes: int = Field(..., description="Access token expiration time in minutes")
    refresh_token_expires_days: int = Field(..., description="Refresh token expiration time in days")

    def get_algorithm(self) -> str:
        """
        Returns the encryption algorithm used.

        Returns:
            str: The encryption algorithm used.
        """
        return self.algorithm

    def get_secret_key(self) -> str:
        """
        Returns the secret key used for encryption.

        Returns:
            str: The secret key used for encryption.
        """
        return self.secret_key

    def get_access_token_expires(self) -> int:
        """
        Returns the expiration time for access tokens in minutes.

        Returns:
            int: The expiration time for access tokens in minutes.
        """
        return self.access_token_expires_minutes

    def get_refresh_token_expires(self) -> int:
        """
        Returns the expiration time for refresh tokens in days.

        Returns:
            int: The expiration time for refresh tokens in days.
        """
        return self.refresh_token_expires_days

    class Config(SettingsConfigDict):
        """
        Configuration for the SecuritySettings model.

        Attributes:
        - env_file (str): The path to the environment file.
        - env_file_encoding (str): The encoding used for the environment file.
        - env_prefix (str): The prefix used for environment variables.
        - extra (str): How to handle extra environment variables.
        """
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "S_"
        extra = "ignore"
```