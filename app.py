from modules.supabase_client import supabase
data = supabase.table("transacciones").select("*").execute
print(data)