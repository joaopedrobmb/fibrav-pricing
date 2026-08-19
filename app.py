from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


class Quotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return "<Quotation %r>" % self.id


from views import *

if __name__ == "__main__":
    app.run(debug=True)
