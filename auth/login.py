import streamlit as st
from modules.supabase_client import supabase
from passlib.hash import bcrypt

def login_db():
    st.title("🔐 Iniciar sesión")

    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    login_button = st.button("Ingresar")

    if login_button:
        if username and password:
            try:
                # Buscar usuario en Supabase
                response = supabase.table("usuarios").select("*").eq("username", username).eq("activo", True).execute()
                usuarios = response.data

                if not usuarios:
                    st.error("❌ Usuario no encontrado o inactivo.")
                    return False, None, None

                usuario = usuarios[0]

                # Verificar contraseña
                if bcrypt.verify(password, usuario['password']):
                    st.success(f"✅ Bienvenido {usuario['nombre']}")
                    return True, usuario['nombre'], usuario['rol']
                else:
                    st.error("❌ Contraseña incorrecta.")
                    return False, None, None

            except Exception as e:
                st.error(f"Error en la autenticación: {e}")
                return False, None, None
        else:
            st.warning("⚠️ Completa todos los campos.")

    return False, None, None


