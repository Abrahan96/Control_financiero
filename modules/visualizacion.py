import streamlit as st
import pandas as pd
import plotly.express as px
from modules.supabase_client import supabase

def visualizacion():
    st.header("📊 Visualización de movimientos")
    
    try:
        #obtener datos de Supabase
        data = supabase.table("transacciones").select("*").eq("activo", True).execute().data
        df = pd.DataFrame(data)
        
        if df.empty:
            st.info("No hay registros activos para mostrar.")
            return
        
        # Preprocesamiento
        df["fecha"] = pd.to_datetime(df["fecha"])
        df = df.sort_values(by="fecha")
        df["monto"] = df["monto"].astype(float)

        # Monto positivo o negativo según tipo
        df["monto_signed"] = df.apply(lambda row: row["monto"] if row["tipo"] == "Ingreso" else -row["monto"], axis=1)
        df["saldo_acumulado"] = df["monto_signed"].cumsum()

        # Mostrar saldo actual
        st.subheader(f"💰 Saldo actual: S/ {df['saldo_acumulado'].iloc[-1]:,.2f}")

        # Mostrar tabla
        st.dataframe(df[["fecha", "descripcion", "tipo", "monto", "categoria", "saldo_acumulado"]])

        # Gráfico de barras: ingresos vs egresos
        fig1 = px.bar(df, x="fecha", y="monto", color="tipo", barmode="relative", title="Ingresos vs Egresos por Fecha")
        st.plotly_chart(fig1, use_container_width=True)

        # Gráfico de línea: saldo en el tiempo
        fig2 = px.line(df, x="fecha", y="saldo_acumulado", title="Saldo acumulado en el tiempo", markers=True)
        st.plotly_chart(fig2, use_container_width=True)

        # Gráfico de torta: categorías
        fig3 = px.pie(df, names="categoria", values="monto", title="Distribución por Categoría", hole=0.4)
        st.plotly_chart(fig3, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Error al cargar visualización: {e}")