from supabase import create_client, Client
import os
#cargando variables desde .env

from dotenv import load_dotenv
load_dotenv()

# obtener datos desde variables de entorno
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

#Conexion

supabase: Client = create_client(url, key)