# -*- coding: utf-8 -*- 
# app/__init__.py

# importações de terceiros
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

# importações locais
from config import app_config

# inicialização da variável do banco de dados (O.R.M)
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "Você deve entrar antes de acessar esta página."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    Bootstrap(app)
    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('erros/403.html', title="Proibido"), 403
        
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('erros/404.html', title="Página não encontrada"), 404
        
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('erros/500.html', title="Erro interno do servidor"), 500

    return app
