# -*- coding: UTF-8 -*-


class BaseConfig:
    APP_NAME = "app_name"
    APP_VERSION = "1"
    SECRET_KEY = "hard to guess string"

    SQLALCHEMY_POOL_SIZE = 100  # 连接池个数
    SQLALCHEMY_POOL_TIMEOUT = 30  # 超时时间，秒
    SQLALCHEMY_POOL_RECYCLE = 3600  # 空连接回收时间，秒
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    ENV = "development"
    DEBUG = True
    LOG_LEVEL = 10
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/db_name?charset=utf8mb4"
    REDIS_URI = "redis://localhost:6379/0"


class TestingConfig(BaseConfig):
    TESTING = True
    LOG_LEVEL = 10
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/db_name?charset=utf8mb4"
    REDIS_URI = "redis://localhost:6379/0"


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql://user_name:user_pwd@127.0.0.1:3306/db_name?charset=utf8mb4"
    REDIS_URI = "redis://localhost:6379/0"


config_map = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
