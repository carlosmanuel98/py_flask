from src.importacion.database.connection import db

class User(db.Model):
    __tablename__ = 'sys_usuarios'
    id_user     = db.Column(db.Integer, primary_key=True)
    first_name  = db.Column(db.String, nullable=True)
    last_name   = db.Column(db.String, nullable=True)
    age         = db.Column(db.Integer, nullable=True)
    gender       = db.Column(db.String, nullable=True)

    def __init__(self, first_name, last_name, age=None, gender=None):
        self.first_name = first_name,
        self.last_name = last_name,
        self.age = age,
        self.gender = gender,
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def to_dict(self):
        return {
           'first_name': self.first_name,
           'last_name': self.last_name,
           'age': self.age,
           'gender': self.gender
        }
        
    

