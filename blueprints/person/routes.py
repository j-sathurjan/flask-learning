from flask import Blueprint, request, jsonify
from .data import data

person_bp = Blueprint("person_bp", __name__, template_folder='templates', static_folder='static')

@person_bp.route("/")
def index():
    """The code simply checks if the variable data exits.
    If it does not, the NameError is raised and an HTTP 404 is returned.
    If data exists and is empty, an HTTP 500 is returned.
    If data exists and is not empty, an HTTP 200 success message is returned.

    Returns:
        _type_: _dictionary is return_
    """
    try:
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            return {"message": f"Data of length {len(data)} found"}
        #If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
        return {"message": "Data is empty"}, 500
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404

@person_bp.route("/name_search")
def name_search():
    """Find a person in the database.
    Returns:
        json: Person if found, with status of 200
        404: If not found
        422: If argument 'q' is missing
    """
    qry=request.args.get('q')
    if qry:
        for person in data:
            if(qry == person['first_name']):
                return person, 200
        return jsonify({"message":"person is not found."}), 404
    return jsonify({"message":"Invalid input parameter, Query parameter 'q' is missing"}), 422

@person_bp.route("/count")
def count():
    """_this return the number of person exist in the data_

    Returns:
        _type_: _length of the data_
    """
    return jsonify({"count":len(data)})

@person_bp.route("/person")
def get_person():
    """return person data

    Returns:
        _type_: dictionary of persons
    """
    if data:
        return data,200
    return jsonify({"message":"no data found"}),404

@person_bp.route("/person/<uuid:id>")
def find_by_uuid(id):
    """it take an argument of type UUID and return the person JSON if found.
    If the person is not found, the method return a 404 with a message of person not found.

    Args:
        uuid (_type_): _person's unique identify id_

    Returns:
        _type_: _person dictionary_
    """
    for person in data:
        if (person['id']==id):
            return person,200
    return jsonify({"message":"person not found."}),404

@person_bp.route("/person/<uuid:id>", methods=['DELETE'])
def delete_by_uuid(id):
    """detele the person matches the uuid given in the url

    Args:
        uuid (_type_): string

    Returns:
        _type_: string
    """
    for person in data:
        if person["id"]==str(id):
            data.remove(person)
            return jsonify({"message":f"the person with the id: {id} deleted."}),204
    return jsonify({"message":"person not found"}),404

@person_bp.route("/person", methods=['POST'])
def add_by_uuid():
    """add a person using post request

    Returns:
        _type_: return message
    """
    try:
        person = request.get_json()
        if not person:
            return jsonify({"message":"invalid input parameter, empty json object passed"}),422
        data.append(person)
        return jsonify({"message":f"person with the id:{person['id']} created."})
    except Exception:
        return jsonify({"message":"something went wrong!"}),415

@person_bp.errorhandler(404)
def api_not_found(error):
    """This function is a custom error handler for 404 Not Found errors
    It is triggered whenever a 404 error occurs within the Flask application
    """
    return {"message": "API not found"}, 404