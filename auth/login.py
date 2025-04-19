import streamlit as st
import streamlit_authenticator as stauth

# Usuarios: puedes cambiarlos o leerlos de un archivo .env si prefieres
nombres = ["Administrador"]
usuarios = ["admin"]
passwords = ["1234"]  # ¡Puedes usar Hash más adelante!

# Encriptar las contraseñas
hashed_passwords = stauth.Hasher(passwords).generate()

# Autenticador
authenticator = stauth.Authenticate(
    names=nombres,
    usernames=usuarios,
    passwords=hashed_passwords,
    cookie_name="control_financiero_login",
    key="random_signature_key",
    cookie_expiry_days=1
)

def login():
    nombre, auth_status, usuario = authenticator.login("Iniciar sesión", "main")

    if auth_status == False:
        st.error("❌ Usuario o contraseña incorrectos")
    elif auth_status == None:
        st.warning("🔒 Ingresa tus credenciales")
    elif auth_status:
        st.success(f"✅ Bienvenido, {nombre}")
        authenticator.logout("Cerrar sesión", "sidebar")
        return True

    return False
