import streamlit as st
from passlib.hash import bcrypt
from modules.supabase_client import supabase  # Asegúrate de tener esto configurado

def login():
    st.title("Iniciar sesión")

    username_input = st.text_input("Usuario").strip().lower()
    password_input = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        try:
            # Buscar al usuario en Supabase
            result = supabase.table("usuarios").select("*").eq("username", username_input).execute()

            if result.data:
                user = result.data[0]

                # Verificar contraseña con bcrypt
                if bcrypt.verify(password_input, user["password"]):
                    st.success(f"✅ Bienvenido, {user['username']}")

                    # Guardar en sesión
                    st.session_state['usuario'] = user['username']
                    st.session_state['rol'] = user.get('rol', 'sin rol')
                    st.session_state['autenticado'] = True

                    return True
                else:
                    st.error("❌ Contraseña incorrecta")
            else:
                st.warning("⚠️ Usuario no encontrado")

        except Exception as e:
            st.error(f"🚫 Error al autenticar: {e}")

    return False



