import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent))
from src.utils.config import RAW_DATA_FILE, CLEANED_DATA_FILE, FEATURED_DATA_FILE

# Class để load và quản lý dữ liệu
class DataLoader:
    
    def __init__(self):
        self.raw_data = None
        self.cleaned_data = None
        self.featured_data = None
    
    # Load dữ liệu gốc từ CSV
    def load_raw_data(self, filepath=None):
        
        if filepath is None:
            filepath = RAW_DATA_FILE
        
        try:
            self.raw_data = pd.read_csv(filepath)
            print(f"Loaded raw data: {self.raw_data.shape[0]:,} rows, {self.raw_data.shape[1]} columns")
            return self.raw_data
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return None
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None
    
    # Load dữ liệu đã làm sạch
    def load_cleaned_data(self, filepath=None):

        if filepath is None:
            filepath = CLEANED_DATA_FILE
        
        try:
            self.cleaned_data = pd.read_csv(filepath)
            print(f"Loaded cleaned data: {self.cleaned_data.shape[0]:,} rows")
            return self.cleaned_data
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return None
    
    # Load dữ liệu đã có features
    def load_featured_data(self, filepath=None):

        if filepath is None:
            filepath = FEATURED_DATA_FILE
        
        try:
            self.featured_data = pd.read_csv(filepath)
            print(f"Loaded featured data: {self.featured_data.shape[0]:,} rows, {self.featured_data.shape[1]} columns")
            return self.featured_data
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return None
    
    # Lấy thông tin cơ bản về dataset
    def get_basic_info(self, df=None):

        if df is None:
            df = self.raw_data
        
        if df is None:
            print(" No data available. Please load data first.")
            return None
        
        info = {
            'shape': df.shape,
            'columns': df.columns.tolist(),
            'dtypes': df.dtypes.to_dict(),
            'missing_values': df.isnull().sum().to_dict(),
            'missing_percentage': (df.isnull().sum() / len(df) * 100).to_dict(),
            'duplicates': df.duplicated().sum(),
            'memory_usage_mb': df.memory_usage(deep=True).sum() / 1024**2
        }
        
        return info
    
    # Lấy thống kê chi tiết cho một cột
    def get_column_stats(self, column_name, df=None):

        if df is None:
            df = self.raw_data
        
        if df is None or column_name not in df.columns:
            return None
        
        col = df[column_name]
        
        if pd.api.types.is_numeric_dtype(col):
            stats = {
                'type': 'numerical',
                'count': col.count(),
                'missing': col.isnull().sum(),
                'mean': col.mean(),
                'median': col.median(),
                'std': col.std(),
                'min': col.min(),
                'max': col.max(),
                'q25': col.quantile(0.25),
                'q75': col.quantile(0.75)
            }
        else:
            stats = {
                'type': 'categorical',
                'count': col.count(),
                'missing': col.isnull().sum(),
                'unique': col.nunique(),
                'top_values': col.value_counts().head(10).to_dict()
            }
        
        return stats
    
    # Lưu DataFrame vào file CSV
    def save_data(self, df, filepath, index=False):

        try:
            df.to_csv(filepath, index=index, encoding='utf-8-sig')
            print(f"Saved data to: {filepath}")
            return True
        except Exception as e:
            print(f"Error saving data: {str(e)}")
            return False
    
    # Lấy mẫu dữ liệu
    def sample_data(self, n=5, df=None, random=False):

        if df is None:
            df = self.raw_data
        
        if df is None:
            return None
        
        if random:
            return df.sample(n=min(n, len(df)))
        else:
            return df.head(n)


# Hàm tiện ích để load nhanh dữ liệu
def quick_load(data_type='featured'):

    loader = DataLoader()
    
    if data_type == 'raw':
        return loader.load_raw_data()
    elif data_type == 'cleaned':
        return loader.load_cleaned_data()
    elif data_type == 'featured':
        return loader.load_featured_data()
    else:
        print(f"Invalid data_type: {data_type}")
        return None


if __name__ == '__main__':
    # Test DataLoader
    print("="*70)
    print("Testing DataLoader")
    print("="*70)
    
    loader = DataLoader()
    
    # Test load raw data
    print("\n1. Loading raw data...")
    df_raw = loader.load_raw_data()
    
    if df_raw is not None:
        print("\n2. Getting basic info...")
        info = loader.get_basic_info(df_raw)
        print(f"   Shape: {info['shape']}")
        print(f"   Duplicates: {info['duplicates']}")
        print(f"   Memory: {info['memory_usage_mb']:.2f} MB")
        
        print("\n3. Sample data:")
        print(loader.sample_data(3, df_raw))
        
        print("\n4. Column stats (salary_min):")
        if 'salary_min' in df_raw.columns:
            stats = loader.get_column_stats('salary_min', df_raw)
            print(stats)
    
    print("\n" + "="*70)
    print("DataLoader test completed!")
    print("="*70)