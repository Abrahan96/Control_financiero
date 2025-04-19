import streamlit as st
import pandas as pd
from modules.supabase_client import supabase

def historial():
    st.header("🗂️ Historial de transacciones")

    try:
        # Obtener solo registros activos
        data = supabase.table("transacciones").select("*").eq("activo", True).execute().data
        df = pd.DataFrame(data)

        if df.empty:
            st.info("No hay registros para mostrar.")
            return

        # Mostrar tabla
        st.dataframe(df)

        # Selección por ID
        id_seleccionado = st.selectbox("Selecciona un ID para editar/eliminar:", df["id"])
        fila = df[df["id"] == id_seleccionado].iloc[0]

        # Mostrar campos editables
        nuevo_tipo = st.selectbox("Tipo", ["Ingreso", "Egreso"], index=["Ingreso", "Egreso"].index(fila["tipo"]))
        nuevo_monto = st.number_input("Monto", min_value=0.01, format="%.2f", value=float(fila["monto"]))
        nueva_descripcion = st.text_area("Descripción", value=fila["descripcion"])
        nueva_fecha = st.date_input("Fecha", value=pd.to_datetime(fila["fecha"]))
        nueva_categoria = st.selectbox("Categoría", [
            "Repuestos", "Movilidad", "Personal", "Alquiler", "Reparación",
            "Mantenimiento", "Préstamo", "Otros", "Epps", "Gasto financiero",
        ], index=0 if fila["categoria"] not in [
            "Repuestos", "Movilidad", "Personal", "Alquiler", "Reparación",
            "Mantenimiento", "Préstamo", "Otros", "Epps", "Gasto financiero",
        ] else [
            "Repuestos", "Movilidad", "Personal", "Alquiler", "Reparación",
            "Mantenimiento", "Préstamo", "Otros", "Epps", "Gasto financiero",
        ].index(fila["categoria"]))

        # Botón actualizar
        if st.button("Actualizar"):
            try:
                supabase.table("transacciones").update({
                    "tipo": nuevo_tipo,
                    "monto": nuevo_monto,
                    "descripcion": nueva_descripcion,
                    "fecha": nueva_fecha.strftime("%Y-%m-%d"),
                    "categoria": nueva_categoria
                }).eq("id", id_seleccionado).execute()
                st.success("✅ Registro actualizado correctamente")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error al actualizar: {e}")

        # Botón eliminar (lógico)
        if st.button("Eliminar"):
            try:
                supabase.table("transacciones").update({"activo": False}).eq("id", id_seleccionado).execute()
                st.success("🗑️ Registro marcado como inactivo")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error al eliminar: {e}")

    except Exception as e:
        st.error(f"❌ Error al cargar historial: {e}")
