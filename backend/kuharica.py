import os

from flask_migrate import Migrate
from flask_cors import CORS

from app import create_app, db
# from app.models.users import User
# from app.models.recipes import Recipe


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

CORS(app, resources={r'/*':{'origins':'http://localhost:8080',
        'allow_headers':'Access-Control-Allow-Origin'}})

migrade = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)