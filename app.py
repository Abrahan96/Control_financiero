import streamlit as st
import time
import pandas as pd
from supabase import create_client, Client
from modules import formulario

#cargando logo
def mostrar_logo():
    st.sidebar.image("Logo.JPG", width=200)
    
st.title("Montargas ML")

formulario