from . import db

class User(db.Model):

    id          =   db.Column(db.Integer, primary_key=True)

    name        =   db.Column(db.String(100))
    age         =   db.Column(db.Integer)
    password    =   db.Column(db.String(150))

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            print(f'Created user {self.name}')
        except Exception as e:
            db.session.rollback()
            print(f'Error saving user {self.name}:', str(e))
        else:
            print(f'created user')
