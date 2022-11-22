import os

base_dir = os.path.dirname(os.path.abspath(__file__))


class BaseConfig:
    """Base configuration"""
    APP_NAME = os.getenv("APP_NAME", "Flask app")
    SECRET_KEY = os.getenv("SECRET_KEY", "secret")
    DEBUG_TB_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


    @staticmethod
    def configure(app):
        pass


class MailConfig:
    """ Повернути налаштування mailtrap :
    MAIL_SERVER ='smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'bdda046ac24020'
    MAIL_PASSWORD = '43925eadee03c6'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    """

    MAIL_SERVER = 'smtp.ukr.net'
    MAIL_PORT = 465
    MAIL_USERNAME = 'a2k_oleksii@ukr.net'
    MAIL_PASSWORD = 'ev4IRK2NUtyze54b'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


class DevelopmentConfig(BaseConfig, MailConfig):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL",
                                         "sqlite:///" + os.path.join(base_dir, "development.sqlite3"))


class ProductionConfig(BaseConfig, MailConfig):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL",
                                         "sqlite:///" + os.path.join(base_dir, "production.sqlite3"))
    WTF_CSRF_ENABLED = True


config = dict(development=DevelopmentConfig, production=ProductionConfig)
