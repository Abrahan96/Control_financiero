import pandas as pd
from modules.supabase_client import supabase
import datetime
import os

def generar_backup_csv():
    try:
        data = supabase.table("transacciones").select("*").eq("activo", True).execute().data
        df = pd.DataFrame(data)

        if df.empty:
            return None, "No hay datos para respaldar."

        # Generar nombre del archivo
        fecha_hoy = datetime.date.today().isoformat()
        nombre_archivo = f"backup_{fecha_hoy}.csv"
        ruta_archivo = os.path.join("data", nombre_archivo)

        # Guardar en local
        df.to_csv(ruta_archivo, index=False)

        return ruta_archivo, None
    except Exception as e:
        return None, f"Error al generar backup: {e}"
