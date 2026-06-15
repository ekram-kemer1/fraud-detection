import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def remove_duplicates(df):
    return df.drop_duplicates()

def convert_datetime(df):
    df["signup_time"] = pd.to_datetime(df["signup_time"])
    df["purchase_time"] = pd.to_datetime(df["purchase_time"])
    return df
import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        print("Data loaded successfully")
        return df

    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    
def convert_datetime(df):

    try:
        df["signup_time"] = pd.to_datetime(df["signup_time"])
        df["purchase_time"] = pd.to_datetime(df["purchase_time"])
        return df

    except Exception as e:
        print(f"Datetime conversion error: {e}")
        return df