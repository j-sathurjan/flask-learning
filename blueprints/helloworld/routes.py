from flask import Blueprint,render_template, make_response, jsonify

helloworld_bp = Blueprint("helloworld_bp", __name__, template_folder='templates', static_folder='static')

@helloworld_bp.route('/')
def index():
    """_this is a function to return home menu_

    Returns:
        _type_: _string_
    """
    return render_template('helloworld/index.html')

@helloworld_bp.route("/greet")
def greet():
    """_this is to greet the users by using json_
    """
    msg = "Hello World"
    return jsonify(message=msg)

@helloworld_bp.route("/no_content")
def no_content():
    """_return a no content message and a custom http status code 204_
    """
    return jsonify({"message":"no content found."}),204

@helloworld_bp.route("/exp")
def index_explicit():
    """Return 'hello it is working!' message with a status code of 200.
    Returns:
        response: A response object containing the message and status code 200.
    """
    resp=make_response({"message":"hello it is working!"})
    resp.status_code=200
    return resp
