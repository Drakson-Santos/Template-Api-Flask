from flask import Flask, jsonify
from dynaconf import FlaskDynaconf
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
FlaskDynaconf(app)
db = SQLAlchemy(app)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Numeric())
    description = db.Column(db.Text)

    @classmethod
    def to_dict(self):
        return {
            'id': 'Test 1',
        }


@app.cli.command()
def createdb():
    """Create sqlite database"""
    db.create_all()


@app.route("/")
def index():
    products = Products.query.all()
    return jsonify(products[0].to_dict())


# if __name__ == "__main__":
#     app.run(debug=True)
