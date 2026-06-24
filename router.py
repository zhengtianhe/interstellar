from views.customer import customer_bp

def register_router(app):
    app.register_blueprint(customer_bp)