import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
import os

path = "data/raw"
archivo = "WA_Fn-UseC_-Telco-Customer-Churn.csv"

#TODO: 1° Generar la función de carga de datos del arhivo lake_dataset
def load_data_raw(path, archivo):
    df = pd.read_csv(os.path.join(path, archivo), sep = ",")
    print("Primera función, la data ya fue cargada")
    return df


def clean_data(df):
    """
    Limpiar los datos eliminando filas con valores nulos.
    """
    
    return print("Estoy en la segunda función del arhivo")

def reemplaza_espacios_blancos(df, columns, replace_value=np.nan):
    """
    Reemplaza los valores en blanco (" ") en las columnas especificadas del DataFrame.
    
    :param df: DataFrame de pandas.
    :param columns: Lista de nombres de columnas donde se realizará el reemplazo.
    :param replace_value: Valor por el cual se reemplazarán los valores en blanco. Por defecto es NaN.
    :return: DataFrame con los valores en blanco reemplazados.
    """
    for column in columns:
        df[column] = df[column].replace(" ", replace_value)
    return df

def imputar_faltantes_knn(df, column, n_neighbors=5):
    """

    """
    imputer = KNNImputer(n_neighbors=n_neighbors)
    df[[column]] = imputer.fit_transform(df[[column]])
    return df

def convert_columns_to_numeric(df, columns):
    """Convierte variable object a numerico

    Args:
        df (_type_): _description_
        columns (_type_): _description_

    Returns:
        _type_: _description_
    """
    for column in columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

# Llamada a la función para cargar los datos
df = load_data_raw(path, archivo)

# Llamada a la función para limpiar los datos
df_cleaned = clean_data(df)