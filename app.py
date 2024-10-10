"""this module is the main app file for crud operation flask application
"""
# Import libraries
from flask import Flask, request, url_for, redirect, render_template
from blueprints.helloworld.routes import helloworld_bp
from blueprints.person.routes import person_bp
from blueprints.mathsweb.routes import mathweb_bp
from blueprints.transaction.routes import transaction_bp

# Instantiate Flask functionality
app=Flask(__name__)
app.register_blueprint(helloworld_bp, url_prefix="/hello"),
app.register_blueprint(person_bp, url_prefix="/person"),
app.register_blueprint(mathweb_bp, url_prefix="/math"),
app.register_blueprint(transaction_bp),

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)