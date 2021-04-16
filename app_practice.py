# Import Flask dependency
from flask import Flask

# Create a new Flask app instance
app = Flask(__name__)

# # Create Flask route(s)
# @app.route('/')
# def hello_world():
#     return 'Hello world'

# Create a new route
@app.route('/')
def print_names():
    numb = 5
    return f'Your number is  {numb}'
