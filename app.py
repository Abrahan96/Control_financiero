import streamlit as st
from modules.formulario import formulario

st.set_page_config(page_title="Control Financiero", layout="centered")

st.sidebar.title("📊 Navegación")

opcion = st.sidebar.radio("Ir a:", ["Formulario"])

if opcion == "Formulario":
    formulario()