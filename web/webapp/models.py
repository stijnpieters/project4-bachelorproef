from . import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def delete_users():
        try:
            num_rows_deleted = db.session.query(User).delete()
            db.session.commit()
            return num_rows_deleted
        except Exception:
            db.session.rollback()
