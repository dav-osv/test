
from app.db import db, BaseModel

class Employe(db.Model,BaseModel): 
    
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    curp = db.Column(db.String(18))
    rfc = db.Column(db.String(13))
    codigo_postal = db.Column(db.Integer)
    fecha_nacimiento = db.Column(db.Date)

    def __init__(self, nombre, curp, rfc, codigo_postal, fecha_nacimiento):
        self.nombre = nombre
        self.curp = curp
        self.rfc = rfc
        self.codigo_postal = codigo_postal
        self.fecha_nacimiento = fecha_nacimiento
   
   
    def __repr__(self):
       # return f'Employe({self.nombre})'
        return "<Title: {}>".format(self.nombre)

    def __str__(self):
        return f'{self.nombre}'