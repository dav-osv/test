from marshmallow import fields, validates_schema,ValidationError
from datetime import datetime
from app.ext import ma


###### Shema para validación de los campos ######

class EmployeSchema(ma.Schema):

    id = fields.Integer(dump_only=True,required=True)
    nombre =  fields.String(required=True)
    curp =  fields.String(required=True)
    rfc =  fields.String(required=True)
    codigo_postal = fields.Integer(required=True)
    fecha_nacimiento = fields.Date(required=True)
     
    @validates_schema
    def validate_fields(self, data, **kwargs):
        
        if len(data['curp'])!=18:
            raise ValidationError("Debe tener 18 caracteres","curp")
        if len(data['rfc'])!= 12 and len(data['rfc'])!= 13:
            raise ValidationError("Debe tener 13 posiciones para personas fisicas o 12 posiciones para personas morales","rfc")
        
        
        try:
           format = "%Y-%m-%d"
           bool(datetime.strptime(str(data['fecha_nacimiento']),format))
        except ValueError:
           raise ValidationError("Debe tener el formato yyyy-mm-dd","fecha_nacimiento")
 