import os
from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).parent.parent.parent
DATA_DIR = BASE_DIR / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
MODELS_DIR = BASE_DIR / 'models'
NOTEBOOKS_DIR = BASE_DIR / 'notebooks'
FIGURES_DIR = NOTEBOOKS_DIR / 'figures'

# File paths
RAW_DATA_FILE = RAW_DATA_DIR / 'jobs.csv'
CLEANED_DATA_FILE = PROCESSED_DATA_DIR / 'cleaned_data.csv'
FEATURED_DATA_FILE = PROCESSED_DATA_DIR / 'featured_data.csv'

# Model paths
BEST_MODEL_PATH = MODELS_DIR / 'best_model.pkl'
SCALER_PATH = MODELS_DIR / 'scaler.pkl'
FEATURES_LIST_PATH = MODELS_DIR / 'features_list.json'
MODEL_INFO_PATH = MODELS_DIR / 'model_info.json'

# Data processing parameters
EXCHANGE_RATE = 25  # USD to VND
TEST_SIZE = 0.2
RANDOM_STATE = 42

# Feature Engineering parameters
EXPERIENCE_MAPPING = {
    'Không yêu cầu': 0, 
    '1-2 năm': 1.5,
    '2-3 năm': 2.5,
    'Dưới 1 năm': 0.5, 
    '2-5 năm': 3.5, 
    '1-3 năm': 2, 
    '1-5 năm': 3, 
    '3-5 năm': 4,
    '3-4 năm': 3.5,
    '5-6 năm': 5.5, 
    '2-4 năm': 3, 
    '4-5 năm': 4.5,
    '5-10 năm': 7.5, 
    '2-10 năm': 6, 
    '5-7 năm': 6, 
    '3-10 năm': 6.5, 
    '1-10 năm': 5.5,
    '3-7 năm': 5, 
    '1-4 năm': 2.5, 
    '5-8 năm': 6.5, 
    '2-7 năm': 4.5, 
    '2-8 năm': 5, 
    '4-6 năm': 5, 
    '5-15 năm': 10, 
    '6-7 năm': 6.5, 
    '2-15 năm': 8.5, 
    'Trên 10 năm': 10.5, 
    '3-15 năm': 9, 
    '2-6 năm': 4, 
    '1-8 năm': 4.5, 
    '3-8 năm': 5.5, 
    '1-7 năm': 4, 
    '4-10 năm': 7, 
    '3-6 năm': 4.5, 
    '5-20 năm': 12.5, 
    '1-15 năm': 8, 
    '7-8 năm': 7.5, 
    '3-20 năm': 11.5, 
    '3-9 năm': 5.5,
    '8-10 năm': 9, 
    '4-7 năm': 5.5, 
    '8-15 năm': 11.5, 
    '2-20 năm': 11, 
    '7-10 năm': 8.5, 
    '4-8 năm': 6, 
    '1-6 năm': 3.5, 
    '2-25 năm': 13.5, 
    '5-25 năm': 15,
    '8-9 năm': 8.5,
    '1-12 năm': 6.5,
    '1-9 năm': 5,
    '1-11 năm': 6,
    '2-14 năm': 8, 
    '9-10 năm': 9.5, 
    '7-15 năm': 12.5,
    '6-8 năm': 7,
    '7-12 năm': 9.5, 
    '7-20 năm': 13.5,
    '3-12 năm': 7.5,
    '6-10 năm': 8,
    '4-20 năm': 12, 
    '1-20 năm': 10.5, 
    '3-17 năm': 10,
    '4-9 năm': 6.5,
    '7-13 năm': 10, 
    '6-11 năm': 8.5,
    '4-12 năm': 8,
    '3-30 năm': 16.5,
    '8-20 năm': 14,
    '4-15 năm': 9.5,
    '1-4': 2.5
}

POSITION_ORDER = ['Chưa cập nhật','Cộng tác viên','Thực tập sinh', 'Nhân viên','Chuyên gia', 'Trưởng nhóm','Trưởng phòng', 'Quản lý', 'Phó giám đốc', 'Giám đốc']

# Salary categories (based on quantiles)
SALARY_CATEGORIES = {
    'Thấp': (0, 0.25),
    'Trung bình thấp': (0.25, 0.5),
    'Trung bình cao': (0.5, 0.75),
    'Cao': (0.75, 1.0)
}

# Outlier detection parameters
IQR_FACTOR = 3.0  # Cho phép outliers nhẹ hơn

# Model parameters
CV_FOLDS = 5
N_TOP_SKILLS = 10
N_TOP_FIELDS = 10
N_TOP_CITIES = 10

# Flask app configuration
FLASK_SECRET_KEY = 'your-secret-key-change-this-in-production'
FLASK_DEBUG = True
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000

# Logging
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def ensure_directories():
    """Tạo các thư mục cần thiết nếu chưa tồn tại"""
    directories = [
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        MODELS_DIR,
        FIGURES_DIR
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

def get_config():
    """Trả về dictionary chứa tất cả config"""
    return {
        'paths': {
            'raw_data': str(RAW_DATA_FILE),
            'cleaned_data': str(CLEANED_DATA_FILE),
            'featured_data': str(FEATURED_DATA_FILE),
            'model': str(BEST_MODEL_PATH),
            'scaler': str(SCALER_PATH)
        },
        'parameters': {
            'exchange_rate': EXCHANGE_RATE,
            'test_size': TEST_SIZE,
            'random_state': RANDOM_STATE,
            'cv_folds': CV_FOLDS
        },
        'mappings': {
            'experience': EXPERIENCE_MAPPING,
            'position_order': POSITION_ORDER
        }
    }

if __name__ == '__main__':
    # Test config
    ensure_directories()
    print("Configuration loaded successfully!")
    print(f"Base directory: {BASE_DIR}")
    print(f"Models directory: {MODELS_DIR}")
    config = get_config()
    print(f"Config keys: {list(config.keys())}")