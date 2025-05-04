from supabase import create_client
from passlib.hash import bcrypt

# Conexión a Supabase
url = "TU_SUPABASE_URL"
key = "TU_SUPABASE_API_KEY"
supabase = create_client(url, key)

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
