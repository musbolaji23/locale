from flask import Flask
from flask_restx import Api
from .config.config import Config
from .models.dbUtil import db
from .models.region import Region
from .region.views import region_namespace
from .state.views import state_namespace
from .lga.views import lga_namespace


def create_app(config=Config):
    app = Flask(__name__)

    app.config.from_object(config)

    # Initialize database and create all tables if they don't exist
    db.init_app(app)
    with app.app_context():
        db.create_all()

    api = Api(app)

    api.add_namespace(lga_namespace, path='/')
    api.add_namespace(region_namespace, path='/')
    api.add_namespace(state_namespace, path='/')

    return app