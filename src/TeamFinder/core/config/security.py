from pydantic_settings import BaseSettings, SettingsConfigDict


class SecuritySettings(BaseSettings):
    algorithm: str
    secret_key: str

    def get_algorithm(self) -> str:
        return self.algorithm

    def get_secret_key(self) -> str:
        return self.secret_key

    model_config = SettingsConfigDict(
        env_file=".env.example", env_file_encoding="utf-8", env_prefix="SECURITY_"
    )
