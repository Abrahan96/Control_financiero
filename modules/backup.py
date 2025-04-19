import streamlit as st
from modules.utils import generar_backup_csv

def backup():
    st.header("💾 Generar Backup de Transacciones")

    if st.button("Generar Backup"):
        archivo, error = generar_backup_csv()
        if error:
            st.error(error)
        else:
            with open(archivo, "rb") as f:
                st.download_button(
                    label="📥 Descargar Backup",
                    data=f,
                    file_name=archivo.split("/")[-1],
                    mime="text/csv"
                )
            st.success("✅ Backup generado con éxito")
