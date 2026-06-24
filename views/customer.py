from flask import Blueprint

customer_bp = Blueprint(
    "customer",
    __name__,
    url_prefix="/customer"
)

@customer_bp.route("/list")
def customer_list():
    return "customer list"

@customer_bp.route("/add")
def customer_add():
    return "customer add"