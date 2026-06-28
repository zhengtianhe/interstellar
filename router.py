from views.auth import auth_bp

def register_router(app):
    app.register_blueprint(auth_bp)