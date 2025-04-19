import streamlit as st
import streamlit_authenticator as stauth

# Usuarios
nombres = ["Administrador"]
usuarios = ["admin"]
contrasenas = ["1234"]  # Contraseñas en texto plano

# Generar hash de contraseñas
hashed_passwords = stauth.Hasher(contrasenas).generate()

# Autenticación
authenticator = stauth.Authenticate(
    names=nombres,
    usernames=usuarios,
    passwords=hashed_passwords,
    cookie_name="control_financiero_login",
    key="firma_secreta",
    cookie_expiry_days=1
)

def login():
    nombre, auth_status, usuario = authenticator.login("Iniciar sesión", "main")

    if auth_status == False:
        st.error("❌ Usuario o contraseña incorrectos")
    elif auth_status == None:
        st.warning("🔒 Por favor ingresa tus credenciales")
    elif auth_status:
        st.success(f"✅ Bienvenido, {nombre}")
        authenticator.logout("Cerrar sesión", "sidebar")
        return True

    return False

