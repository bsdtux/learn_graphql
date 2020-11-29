import os

BASE = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    """Base Configuration File"""
    DEBUG=False
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class DevConfig(BaseConfig):
    """Development Configuration

    Args:
        BaseConfig (Object): Parent configuration
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE, 'data/dev.sqlite')


class TestConfig(BaseConfig):
    """Testing Configuration

    Args:
        BaseConfig (Object): Parent configuration
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE, 'data/test.sqlite')


class ProdConfig(BaseConfig):
    """[summary]

    Args:
        BaseConfig (Object): Parent configuration
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE, 'data/prod.sqlite')


config_factory = {
    'development': DevConfig, 'testing': TestConfig, 'production': ProdConfig}