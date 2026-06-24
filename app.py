from flask import Flask
from router import register_router
def create_app():
    app = Flask(__name__)
    register_router(app)
    return app