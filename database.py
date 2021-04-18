from app import db,fields, marshal_with

class UserModel(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(100), nullable=False, unique=True)
    Pass = db.Column(db.String(16), nullable=False)

    def __repr__(self):
        return f"Users(name = {name}, User Name = {UserName}, Password = {password})"
resourse_fields = {
    'id':fields.String,
    'UserName':fields.String,
    'Pass':fields.String
}