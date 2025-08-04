import pandas as pd
import datetime

#Convierte todos los valores en un DataFrame a tipos compatibles con JSON
def sanitize_for_json(value):
    if isinstance(value, (datetime.date, datetime.datetime, datetime.time)):
        return value.isoformat()  # Convierte a string ISO: "08:30:00"
    return value

def excel_to_json(file_path):
    try:
        df = pd.read_excel(file_path) #Lee la hoja 1 por defecto
        # Rellena celdas vacías con el valor anterior (para columnas con celdas combinadas)
        df.fillna(method="ffill", inplace=True)
        # Aplica la función de sanitización a todo el DataFrame
        data = df.applymap(sanitize_for_json).to_dict(orient="records")
        return data
    except Exception as e:
        raise Exception(f"Error leyendo el Excel: {str(e)}") #Lanza error