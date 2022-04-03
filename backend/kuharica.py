import os

from flask_migrate import Migrate

from app import create_app, db
# from app.models.users import User
# from app.models.recipes import Recipe


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrade = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)