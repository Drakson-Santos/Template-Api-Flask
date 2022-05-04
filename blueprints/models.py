from extensions.database import db

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