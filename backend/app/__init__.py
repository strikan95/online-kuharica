from flask import Flask
from config import config as cfg
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_jwt_extended import JWTManager

db = SQLAlchemy(metadata=MetaData(naming_convention={
    'pk': 'pk_%(table_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'ix': 'ix_%(table_name)s_%(column_0_name)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
}))

jwt = JWTManager()

def create_app(config_name):
    mApp = Flask(__name__)
    mApp.config.from_object(cfg[config_name])
    cfg[config_name].init_app(mApp)

    db.init_app(mApp)
    jwt.init_app(mApp)

    from .spa import spa as spa
    mApp.register_blueprint(spa)

    from .api import api_bp as api
    mApp.register_blueprint(api)
    return mApp