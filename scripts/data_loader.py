import pandas as pd

def load_data(path, sheet_name=None, ignore_index_col=True):
   
    if path.endswith('.csv'):
        df = pd.read_csv(path)

        if ignore_index_col:
            posibles_indices = ['Unnamed: 0', 'index', 'Index']
            for col in posibles_indices:
                if col in df.columns:
                    df = df.drop(columns=[col])
                    print(f"Columna de índice anterior '{col}' eliminada automáticamente.")
                    break

    elif path.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(path, sheet_name=sheet_name)

    else:
        raise ValueError('❌ Formato no encontrado. Use .csv o .xls')

    print(f'Archivo cargado correctamente: {path} ({df.shape[0]} filas, {df.shape[1]} columnas)')
    return df
