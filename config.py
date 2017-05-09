# -*- coding: utf-8 -*-
# config.py

class Config(object):
    """
    Configurações em comun
    """

    # coloque qualquer configuração comum à todos os ambientes nesta linha


class DevelopmentConfig(Config):
    """
    Configurações de desenvolvimento
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Configurações de produção
    """

    DEBUG = False

app_config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
}
