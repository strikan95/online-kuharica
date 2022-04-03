from flask import render_template
from . import spa

@spa.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")