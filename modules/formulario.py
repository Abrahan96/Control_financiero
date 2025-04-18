import streamlit as st
import time
from supabase import create_client, Client
from dotenv import load_dotenv
import os


def formulario():
    st.header("Ingresar movimiento")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Egreso"])