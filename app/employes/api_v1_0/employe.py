from marshmallow import ValidationError
from flask_restful import Resource
from flask import request
from ..models import Employe
from .shemas import EmployeSchema
film_schema = EmployeSchema()
from app.auth import auth

###############################    CRUD DE EMPLEADOS ##################################################################

class Employees(Resource):

    ### decoradores de acceso / roles  ###
     
    method_decorators={
        'get' : [auth.login_required(role=['administrador','operador','supervisor'])],
        'post': [auth.login_required(role='administrador')]
    }



    # Obtener una lista de empleados  #

    def get(self):
        try:
            
           employees = film_schema.dump(Employe.get_all(), many=True)
           return {'code': 200,'message': 'success', 'content': employees},200
        except Exception as message:
           return {'code': 500,'message': 'error', 'content': str(message)},500

    # Crear un empleado #

    def post(self):

        try:

            data = request.get_json()

            
            employe_dict = film_schema.load(data)



            employe = Employe( nombre=employe_dict['nombre'],
                            curp=employe_dict['curp'],
                            rfc=employe_dict['rfc'],
                            codigo_postal=employe_dict['codigo_postal'],
                            fecha_nacimiento=employe_dict['fecha_nacimiento']
                            )
            
            employe.save()

            newEmploye = film_schema.dump(employe)

            
            return {'code': 201,'message': 'success', 'content': newEmploye},201

        except Exception as message:
           return {'code': 500,'message': 'error', 'content': str(message)},500

 


# Obtener un Empleado  #
class EmployeShow(Resource):
    
    method_decorators={
        'get' : [auth.login_required(role=['administrador','operador','supervisor'])],
    }

    def get(self, employe_id):

        try:

            employe = Employe.get_by_id(employe_id)
            if employe is None:
               return {'code': 404,'message': 'El empleado no existe (not found)', 'content': None},404
            
            showEmploye = film_schema.dump(employe)
         
            return {'code': 200,'message': 'success', 'content': showEmploye},200
        except Exception as message:
           return  {'code': 500,'message': 'error', 'content': str(message)},500


# Actualizar un empleado
class EmployeUpdate(Resource):

    method_decorators={
        'put' : [auth.login_required(role=['administrador','supervisor'])],
    }

    def put(self,employe_id):
        try:

            employe = Employe.get_by_id(employe_id)
    
            if employe is None:
                return {'code': 404,'message': 'not_found', 'content': None},404

            data = request.get_json()
            employe_dict = film_schema.load(data)

            currentEmploye =  Employe.simple_filter(id = employe_id)
            currentEmploye.nombre =  employe_dict['nombre']
            currentEmploye.curp = employe_dict['curp']
            currentEmploye.rfc = employe_dict['rfc']
            currentEmploye.codigo_postal = employe_dict['codigo_postal']
            currentEmploye.fecha_nacimiento = employe_dict['fecha_nacimiento']
            currentEmploye.update()

            return {'code': 201,'message': 'success', 'content': film_schema.dump(currentEmploye)},201

        except Exception as message:
            return  {'code': 500,'message': 'error', 'content': str(message)},500

# Eliminar un empleado  
class EmployeDelete(Resource):
    
    method_decorators={
        'delete' : [auth.login_required(role=['administrador'])],
    }

    def delete(self,employe_id):
  
        try:
            employe = Employe.get_by_id(employe_id)

            if employe is None:
               return {'code': 404,'message': 'El empleado no existe(not_found)', 'content': None},404
        
            employe.delete()
            return {'code': 200,'message': 'success', 'content': None},200

        except Exception as message:
           return {'code': 500,'message': 'error', 'content': str(message)},500
        
         