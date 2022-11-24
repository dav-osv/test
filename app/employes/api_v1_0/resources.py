from flask import  Blueprint
from flask_restful import Api
from .employe import Employees
from .employe import EmployeShow
from .employe import EmployeDelete
from .employe import EmployeUpdate
from .login import Login 

employes_v1_0 = Blueprint('films_v1_0_bp', __name__)


api = Api(employes_v1_0)


## Rutas de empleado ## 

api.add_resource(Employees, '/api/v1.0/employe/', endpoint='employe')
api.add_resource(EmployeShow, '/api/v1.0/employe/<int:employe_id>', endpoint='employe/show')
api.add_resource(EmployeUpdate, '/api/v1.0/employe/<int:employe_id>', endpoint='employe/update')
api.add_resource(EmployeDelete, '/api/v1.0/employe/<int:employe_id>', endpoint='employe/delete')


##  Rutas de login   ##
api.add_resource(Login,'/api/v1.0/login',endpoint="login")