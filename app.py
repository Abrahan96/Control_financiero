import streamlit as st
from modules.formulario import formulario
from modules.visualizacion import visualizacion
from modules.historial import historial
from modules.backup import backup
from auth.login import login


st.set_page_config(page_title="Control Financiero", layout="centered")

if login():

    st.sidebar.title("📊 Navegación")

    opcion = st.sidebar.radio("Ir a:", ["Formulario", "Visualización", "Historial", "Backup"])

    if opcion == "Formulario":
        formulario()
    elif opcion == "Visualización":
        visualizacion()
    elif opcion == "Historial":
        historial()
    elif opcion == "Backup":
        backup()