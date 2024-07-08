from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_HOST: str
    APP_PORT: int
    SECRET_KEY: str
    SERVER_METADATA_URL: str
    SQLALCHEMY_DATABASE_URI: str
    ALLOWED_HOSTS: str
    DOMAIN_NAME: str


settings = Settings()

ALLOWED_HOSTS = [host.strip() for host in settings.ALLOWED_HOSTS.split(",")]
