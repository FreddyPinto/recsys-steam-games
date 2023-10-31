import pandas as pd
import os

def load_data():
    data_dir = os.path.join(os.path.dirname(__file__),'..', 'data', 'processed')  # Ruta a tu directorio 'data/processed'
    
    df_endpoint1 = pd.read_parquet(os.path.join(data_dir, 'endpoint1.parquet'))
    df_endpoint2 = pd.read_parquet(os.path.join(data_dir, 'endpoint2.parquet'))
    df_endpoint3 = pd.read_parquet(os.path.join(data_dir, 'endpoint3.parquet'))
    df_endpoint4 = pd.read_parquet(os.path.join(data_dir, 'endpoint4.parquet'))

    return df_endpoint1, df_endpoint2, df_endpoint3, df_endpoint4

df_endpoint1, df_endpoint2, df_endpoint3, df_endpoint4 = load_data()
