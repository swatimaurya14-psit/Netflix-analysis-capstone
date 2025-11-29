# src/data_cleaning.py

import pandas as pd

def load_data(file_path):
    """
    CSV ya Excel file load karne ka function.
    
    Parameters:
    file_path (str): Dataset ka path
    
    Returns:
    pd.DataFrame: Loaded dataframe
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully! Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print("Error: File not found. Please check the path.")
        return None

def clean_data(df):
    """
    Data cleaning aur preprocessing function.
    
    Steps:
    - Duplicate rows remove karna
    - Missing values handle karna
    - Columns ko proper format me lana
    
    Parameters:
    df (pd.DataFrame): Original dataframe
    
    Returns:
    pd.DataFrame: Cleaned dataframe
    """
    if df is None:
        return None
    
    # 1️⃣ Drop duplicates
    df = df.drop_duplicates()
    
    # 2️⃣ Fill missing values
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')
    df['rating'] = df['rating'].fillna('Not Rated')
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    
    # 3️⃣ Strip whitespace in string columns
    str_cols = df.select_dtypes(include='object').columns
    for col in str_cols:
        df[col] = df[col].str.strip()
    
    # 4️⃣ Reset index
    df = df.reset_index(drop=True)
    
    print(f"Data cleaned successfully! Shape: {df.shape}")
    return df
