from app import app
from db import db

# this is all to prevent circular imports
db.init_app(app)

# this will run before the app takes any request
# this is based on the import statements
@app.before_first_request
def create_tables():
    db.create_all()
