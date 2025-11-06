import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from app.models import User, Post
from app import app as flask_app  # ✅ import Flask instance safely
import app.routes  # ✅ force route registration


@flask_app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}


if __name__ == "__main__":
    flask_app.run(debug=True)
