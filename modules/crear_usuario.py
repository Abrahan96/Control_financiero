from passlib.hash import bcrypt
from modules.supabase_client import supabase

# Datos del nuevo usuario
nuevo_usuario = {
    "username": "admin",
    "password": bcrypt.hash("1234"),  # Contraseña encriptada
    "nombre": "Administrador General",
    "rol": "admin",
    "activo": True
}

# Insertar en la tabla usuarios
respuesta = supabase.table("usuarios").insert(nuevo_usuario).execute()

print("✅ Usuario insertado:", respuesta.data)
