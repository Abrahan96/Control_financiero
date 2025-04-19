import streamlit as st
from modules.formulario import formulario
from modules.visualización import visualizacion

st.set_page_config(page_title="Control Financiero", layout="centered")

st.sidebar.title("📊 Navegación")

opcion = st.sidebar.radio("Ir a:", ["Formulario", "Visualizacion"])

if opcion == "Formulario":
    formulario()
elif opcion == "Visualizacion":
    visualizacion()