import os

from flask_migrate import Migrate
from flask_cors import CORS

from app import create_app, db
# from app.models.users import User
# from app.models.recipes import Recipe


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

CORS(app, supports_credentials=True)

# CORS(app, resources={r'/*':{
#         "Access-Control-Allow-Origin": "*",
#         "Access-Control-Allow-Credentials": "true",
#         "Access-Control-Allow-Methods": "GET,HEAD,OPTIONS,POST,PUT",
#         "Access-Control-Allow-Headers": "Access-Control-Allow-Headers,Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"}})

# CORS(app, supports_credentials=True)
# app.config['CORS_HEADERS'] = 'Content-Type'

migrade = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)