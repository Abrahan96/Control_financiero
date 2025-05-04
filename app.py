import streamlit as st
from modules.formulario import formulario
from modules.visualizacion import visualizacion
from modules.historial import historial
from modules.backup import backup
from auth.login import login

# Configuración de la página
st.set_page_config(page_title="Control Financiero", layout="centered")

# Inicializar el estado de sesión
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

# Si no está autenticado, mostrar login
if not st.session_state.autenticado:
    usuario_autenticado = login()
    if usuario_autenticado:
        st.session_state.autenticado = True
    else:
        st.stop()

# Interfaz de navegación
st.sidebar.title("📊 Navegación")
opcion = st.sidebar.radio("Ir a:", ["Formulario", "Visualización", "Historial", "Backup", "Cerrar sesión"])

# Mostrar página correspondiente
if opcion == "Formulario":
    formulario()
elif opcion == "Visualización":
    visualizacion()
elif opcion == "Historial":
    historial()
elif opcion == "Backup":
    backup()
elif opcion == "Cerrar sesión":
    st.session_state.autenticado = False
    st.experimental_rerun()  # Refrescar la app para volver al login
