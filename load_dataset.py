import pandas as pd
from pathlib import Path
# data/load_dataset.py
def load_training_data():
    # Your implementation here
    pass

def load_training_data():
    try:
        data_dir = Path(__file__).parent.parent / 'data'
        csv_path = data_dir / 'processed' / 'emails.csv'
        df = pd.read_csv(csv_path)
        return df["content"].values, df["is_phishing"].values
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None, None