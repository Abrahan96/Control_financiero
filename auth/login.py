import streamlit as st
import streamlit_authenticator as stauth

# Generar hash de contraseñas
contrasenas = ["1234"]
hashed_passwords = stauth.Hasher(contrasenas).generate()

# Configuración en formato diccionario
config = {
    "credentials": {
        "usernames": {
            "admin": {
                "name": "Administrador",
                "password": hashed_passwords[0]
            }
        }
    },
    "cookie": {
        "name": "control_financiero_login",
        "key": "firma_secreta",
        "expiry_days": 1
    },
    "preauthorized": {
        "emails": []
    }
}

# Crear autenticador
authenticator = stauth.Authenticate(config)


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
