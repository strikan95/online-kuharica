from flask import Blueprint

spa = Blueprint('spa', __name__)

from . import views