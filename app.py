import streamlit as st
from modules.formulario import formulario
from modules.visualizacion import visualizacion
from modules.historial import historial
from modules.backup import backup
from auth.login import login

# Configurar la página
st.set_page_config(page_title="Control Financiero", layout="centered")

# Inicializar el estado de autenticación
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

# Verificar autenticación
if not st.session_state.autenticado:
    usuario_autenticado = login()
    if usuario_autenticado:
        st.session_state.autenticado = True
    else:
        st.stop()

# Sidebar y navegación
st.sidebar.title("📊 Navegación")

# Botón para cerrar sesión
if st.sidebar.button("🔒 Cerrar sesión"):
    st.session_state.autenticado = False
    st.success("Sesión cerrada correctamente. Recarga la página para iniciar nuevamente.")
    st.stop()

# Menú de navegación
opcion = st.sidebar.radio("Ir a:", ["Formulario", "Visualización", "Historial", "Backup"])

# Mostrar página correspondiente
if opcion == "Formulario":
    formulario()
elif opcion == "Visualización":
    visualizacion()
elif opcion == "Historial":
    historial()
elif opcion == "Backup":
    backup()

