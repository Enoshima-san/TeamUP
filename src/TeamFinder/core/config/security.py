from pydantic_settings import BaseSettings, SettingsConfigDict


class SecuritySettings(BaseSettings):
    algorithm: str
    secret_key: str
    access_token_expires: int
    refresh_token_expires: int

    def get_algorithm(self) -> str:
        return self.algorithm

    def get_secret_key(self) -> str:
        return self.secret_key

    def get_access_token_expires(self) -> int:
        return self.access_token_expires

    def get_refresh_token_expires(self) -> int:
        return self.refresh_token_expires

    model_config = SettingsConfigDict(
        env_file=".env.example", env_file_encoding="utf-8", env_prefix="S_"
    )
