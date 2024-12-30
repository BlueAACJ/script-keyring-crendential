import keyring
import keyring.credentials 

#   Estructura URL postgreSQL
#   postgresql://postgres:azocar@localhost:5432/Nombre de la BD
#   user - password - localhost - puerto - nombreBD

# Guardar crendenciales de Windows
# nombreDelServicio = Nombre que le querramos poner al servicio
# NombreDeUsuario = Nombre de usuario que querramos ponerle a la credencial
# password = URL de la Base de Datos, al guardarle como password se guarda cifrada
x=keyring.set_password(service_name="DemoCamioneraGranicSA", username="DemoCamioneraGranicSA",password="postgresql://postgres:azocar@localhost:5432/DemoCamioneraGranicSA")

# Acceder a la direccion de  de Windows
URL = keyring.get_credential("DemoCamioneraGranicSA","DemoCamioneraGranicSA")

# Acceder a la contrasena o Credencial cifrada
print(URL.password)
