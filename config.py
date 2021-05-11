import os
from dataclasses import dataclass
from logger import logger

@dataclass
class DBConfig:
    sql_username: str = os.getenv('USERNAME', 'user')
    sql_password: str = os.getenv('PASSWORD', 'password')
    sql_db_name: str = 'demo_db'
    sql_url: str = 'sqlite:///./sql_app.db'


@dataclass
class BaseConfig(DBConfig):
    name: str = 'Boiler'
    is_debug: str = True
    host: str = "0.0.0.0"
    port: int = 5005


@dataclass
class LocalConfig(BaseConfig):
    pass


@dataclass
class DevConfig(BaseConfig):
    sql_url: str = f'postgresql://{BaseConfig.sql_username}:{BaseConfig.sql_password}@postgresserver/{BaseConfig.sql_db_name}'
    pass


@dataclass
class StageConfig(BaseConfig):
    sql_url: str = f'postgresql://{BaseConfig.sql_username}:{BaseConfig.sql_password}@postgresserver/{BaseConfig.sql_db_name}'


@dataclass
class ProdConfig(BaseConfig):
    sql_url: str = f'postgresql://{BaseConfig.sql_username}:{BaseConfig.sql_password}@postgresserver/{BaseConfig.sql_db_name}'
    pass


env_configurations = {
    'local': LocalConfig(),
    'dev': DevConfig(),
    'stage': StageConfig(),
    'prod': ProdConfig()}

env = os.getenv('ENV', 'local')
configuration = env_configurations.get(env, None)
logger.info(f'Config init done, Running {env} configuration')