import streamlit as st

st.set_page_config(page_title="Control Financiero", layout="centered")

from modules.formulario import formulario
from modules.visualizacion import visualizacion
from modules.historial import historial
from modules.backup import backup
from auth.login import login_db

st.set_page_config(page_title="Control Financiero", layout="centered")

is_authenticated, nombre_usuario, rol_usuario = login()

if is_authenticated:
    st.sidebar.title(f"📊 Navegación - {nombre_usuario}")

    opcion = st.sidebar.radio("Ir a:", ["Formulario", "Visualización", "Historial", "Backup"])

    if opcion == "Formulario":
        formulario()
    elif opcion == "Visualización":
        visualizacion()
    elif opcion == "Historial":
        historial()
    elif opcion == "Backup":
        backup()
else:
    st.stop()