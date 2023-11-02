from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    log_file: str = './data/weblog.csv'

    model_config = SettingsConfigDict(env_file='../.env')

settings = Settings()