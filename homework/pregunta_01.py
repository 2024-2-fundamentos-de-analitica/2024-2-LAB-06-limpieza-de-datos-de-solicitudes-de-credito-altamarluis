"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os

def pregunta_01():
    # Definir la ruta del archivo de entrada y salida
    input_path = "files/input/solicitudes_de_credito.csv"
    output_path = "files/output/solicitudes_de_credito.csv"
    
    # Verificar si el archivo de entrada existe
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"El archivo {input_path} no existe.")
    
    # Cargar el archivo CSV
    df = pd.read_csv(input_path, sep=";", index_col=0)
    
    # Normalización de datos
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower().str.strip()
    df["idea_negocio"] = df["idea_negocio"].str.lower().str.replace("_", " ").str.replace("-", " ").str.strip()
    df["barrio"] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    df["línea_credito"] = df["línea_credito"].str.lower().str.strip().str.replace("_", " ").str.replace("-", " ").str.strip()
    
    # Conversión de tipos de datos
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    df["monto_del_credito"] = df["monto_del_credito"].str.strip().str.replace("$", "").str.replace(",", "").str.replace(".00", "").astype(int)
    
    # Manejo de fechas
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
    ).combine_first(
        pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
    )
    
    # Eliminar registros duplicados y valores nulos
    df = df.drop_duplicates()
    df = df.dropna()
    
    # Guardar el archivo limpio en la ruta de salida
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, sep=';', index=False)

# Ejecutar la función si el script se ejecuta directamente
if __name__ == "__main__":
    pregunta_01()
