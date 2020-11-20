class Config:
    DEBUG = False


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


config = {
    'dev': DevConfig,
    'test': TestConfig
}
