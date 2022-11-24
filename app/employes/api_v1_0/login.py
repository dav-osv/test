from flask_restful import Resource,request
from app.bd.users import users
from app import token_serialize
class Login (Resource):
   
    #### Metodo de verificacion de user-password  ###

    def post(self):
        _user = request.get_json().get('usuario')
        _passw = request.get_json().get('password')

        for user in users:
            if _user == user.get('user') and _passw == user.get('passw'):
                token = token_serialize.dumps(dict(user = _user))
                return dict(message='success!', token = token), 201
        return dict(message = 'Error de credenciales'),400 