import streamlit as st
import datetime
from modules.supabase_client import supabase

def formulario():
    st.header(" 📥 Registrar movimiento")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Egreso"])
    monto = st.number_input("Monto", min_value=0.01, step=0.01, format="%.2f")
    descripcion = st.text_area("Descripción")
    fecha = st.date_input("Fecha", value=datetime.date.today())
    categoria = st.selectbox("Categoría",["Repuestos","Movilidad","Personal","Alquiler","Reparación","Mantenimiento","Préstamo","Otros","Epps","Gasto financiero"])

    if st.button("Registrar"):
        if monto and descripcion:
            data ={
                "tipo": tipo,
                "monto": monto,
                "descripcion": descripcion,
                "fecha": fecha.strftime("%Y-%m-%d"),
                "categoria": categoria,
                "activo": True
            }
        
            try:
                supabase.table("transacciones").insert(data).execute()
                st.success("✅ Movimiento registrado correctamente")
            except Exception as e:
                st.error(f"❌ Error al registrar: {e}")
        else:
                st.warning("⚠️ Completa todos los campos obligatorios")