from flask import Blueprint, request, render_template
from packages.maths.mathematics import summation, subtraction, multiplication

mathweb_bp = Blueprint("mathweb_bp", __name__, template_folder='templates', static_folder='static')

@mathweb_bp.route("/")
def index():
    return render_template("mathsweb/index.html")

@mathweb_bp.route("/sum")
def summation_route():
    """This accept parameters num1 and num 2 and then returns summation of two as string

    Returns:
        _type_: _description_
    """
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    result = summation(num1, num2)
    return str(result)

@mathweb_bp.route("/sub")
def subtraction_route():
    """This accept parameters num1 and num 2 and then returns subraction of two as string

    Returns:
        _type_: _description_
    """
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    result = subtraction(num1, num2)
    return str(result)

@mathweb_bp.route("/mul")
def multiplication_route():
    """This accept parameters num1 and num 2 and then returns multiplication of two as string

    Returns:
        _type_: _description_
    """
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    result = multiplication(num1, num2)
    return str(result)
