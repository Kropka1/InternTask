from dotenv import load_dotenv
from pydantic.env_settings import BaseSettings
load_dotenv()


class Settings(BaseSettings):
    extdb_port: int
    intdb_port: int
    db_user: str
    db_image: str
    db_password: str
    db_host: str
    postgres_db: str
    postgres_driver: str

    @property
    def db_url(self):
        return f'{self.postgres_driver}://{self.db_user}:{self.db_password}@{self.db_host}:{self.extdb_port}/{self.postgres_db}'


settings = Settings()


if __name__ == "__main__":
    print(settings.db_host)
