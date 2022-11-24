
from app import create_app
app = create_app()


############                                      CONFIGURACION              ##########

# Librerias ocupadas: 

  # pip install Flask-HTTPAuth
  # pip install flask 
  # pip install flask_restful 
  # pip install flask_sqlalchemy 
  # pip install flask_migrate 
  # pip install flask_marshmallow 
  # pip install marshmallow-sqlalchemy


# 1. Importar colección (test) en postman para probar API-REST
         #dominio local: 127.0.0.1


# 2. Crear BD "test" en mysql. 
#              Para mas información verificar app/config. 
#              Credenciales user: root password: Ninguno 




# 3. Correr migración para crear la tabla empleado en la BD con el siguiente comando
    #  flask db upgrade


# 4. Iniciar aplicación  con el siguiente comando : flask run



#####  Usuarios  y roles de autoentificación   ######

 # user='administrador', passw= 'admin1234', role= 'administrador',
 # user='operador', passw= 'operador1234', role= 'operador'),
 # user='supervisor', passw= 'supervisor1234', role= 'supervisor')




## DESCRIPCIÓN DE COLECCION EN POSTMAN ##

#login (POST):            Inicio de sesión devuelve un token de autoentificación
#listEmployes (GET):      Devuelve una lista de empleados, recibe en los headers el token de autoentificación
#showEmploye (GET):       Devuelve 1 empleado ,se le pasa un argumento de tipo entero como parametro, recibe en los headers el token de autoentificación
#createEmploye (POST):    Crea un empleado de tipo json en body, recibe en los headers el token de autoentificación
#updateEmploye (PUT):     Actualiza un empleado de tipo json en body,  recibe en los headers el token de autoentificación
#deleteEmploye  (DELETE): Elimina un empleado, se le pasa un argumento de tipo entero como parametro, recibe en los headers el token de autuentificación


## En la carpeta test se encuentra  algunas  evidencias del funcionamiento de la API-REST EN POSTMAN