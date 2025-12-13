# CẤU TRÚC DỰ ÁN DỰ ĐOÁN LƯƠNG

## 1. MÔI TRƯỜNG PHÁT TRIỂN

### 1.1. Công cụ cần thiết

**Python:** Phiên bản 3.8 trở lên (khuyến nghị 3.9 hoặc 3.10)

**IDE/Editor:** 
- **Jupyter Notebook/JupyterLab** - Cho giai đoạn phân tích và thử nghiệm
- **VS Code** - Cho giai đoạn phát triển ứng dụng Flask

**Quản lý môi trường ảo:**
- `venv` (built-in Python)
- `conda` (Anaconda/Miniconda)

### 1.2. Cài đặt môi trường

#### Bước 1: Tạo thư mục dự án
```bash
mkdir salary-prediction-project
cd salary-prediction-project
```

#### Bước 2: Tạo môi trường ảo
```bash
# Sử dụng venv
python -m venv venv

# Kích hoạt môi trường
source venv/bin/activate
```

#### Bước 3: Cài đặt thư viện cần thiết
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
pip install jupyter ipykernel
pip install wordcloud
pip install flask flask-cors
pip install joblib pickle-mixin
pip install xgboost lightgbm
```

## 2. CẤU TRÚC THỨ CẤP DỰ ÁN

```
salary-prediction-project/
│
├── data/                          # Thư mục chứa dữ liệu
│   ├── raw/                       # Dữ liệu gốc
│   │   └── jobs.csv
│   ├── processed/                 # Dữ liệu đã xử lý
│   │   ├── cleaned_data.csv
│   │   └── train_test_data.pkl
│   └── external/                  # Dữ liệu bổ sung (nếu có)
│
├── notebooks/                     # Jupyter notebooks cho phân tích
│   ├── 01_data_exploration.ipynb  # Khám phá dữ liệu ban đầu
│   ├── 02_data_cleaning.ipynb     # Làm sạch dữ liệu
│   ├── 03_feature_engineering.ipynb # Tạo features
│   ├── 04_visualization.ipynb     # Trực quan hóa
│   ├── 05_modeling.ipynb          # Xây dựng mô hình
│   └── 06_evaluation.ipynb        # Đánh giá mô hình
│
├── src/                           # Source code chính
│   ├── __init__.py
│   │
│   ├── data/                      # Xử lý dữ liệu
│   │   ├── __init__.py
│   │   ├── data_loader.py         # Load dữ liệu
│   │   ├── data_cleaner.py        # Làm sạch dữ liệu
│   │   └── data_transformer.py    # Biến đổi dữ liệu
│   │
│   ├── features/                  # Feature engineering
│   │   ├── __init__.py
│   │   ├── feature_builder.py     # Tạo features mới
│   │   └── feature_selector.py    # Chọn features
│   │
│   ├── models/                    # Mô hình machine learning
│   │   ├── __init__.py
│   │   ├── base_model.py          # Lớp base cho mô hình
│   │   ├── clustering.py          # Mô hình phân cụm
│   │   ├── classification.py      # Mô hình phân lớp
│   │   ├── regression.py          # Mô hình hồi quy
│   │   └── predictor.py           # Dự đoán
│   │
│   ├── visualization/             # Trực quan hóa
│   │   ├── __init__.py
│   │   ├── plots.py               # Các hàm vẽ biểu đồ
│   │   └── dashboards.py          # Dashboard tổng hợp
│   │
│   └── utils/                     # Tiện ích
│       ├── __init__.py
│       ├── config.py              # Cấu hình
│       └── helpers.py             # Hàm hỗ trợ
│
├── models/                        # Lưu mô hình đã train
│   ├── model_v1.pkl
│   ├── scaler.pkl
│   ├── encoder.pkl
│   └── best_model.pkl
│
├── app/                           # Flask application
│   ├── __init__.py
│   ├── routes.py                  # Định nghĩa routes
│   ├── forms.py                   # Form xử lý input
│   │
│   ├── templates/                 # HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── predict.html
│   │   └── results.html
│   │
│   └── static/                    # Static files
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── main.js
│       └── images/
│
├── tests/                         # Unit tests
│   ├── __init__.py
│   ├── test_data_processing.py
│   ├── test_models.py
│   └── test_api.py
│
├── docs/                          # Documentation
│   ├── api_documentation.md
│   └── user_guide.md
│
├── config/                        # Configuration files
│   ├── config.yaml
│   └── logging_config.yaml
│
├── scripts/                       # Scripts tiện ích
│   ├── train_model.py             # Script train mô hình
│   ├── evaluate_model.py          # Script đánh giá
│   └── deploy.py                  # Script deploy
│
├── requirements.txt               # Dependencies
├── setup.py                       # Package setup
├── .gitignore                     # Git ignore
├── README.md                      # Mô tả dự án
├── run.py                         # Entry point cho Flask app
└── LICENSE
```

## 3. QUY TRÌNH LÀM VIỆC TỪNG BƯỚC

### Giai đoạn 1: Phân tích và thử nghiệm (Notebooks)

**Bước 1:** Khám phá dữ liệu trong `01_data_exploration.ipynb`
- Load dữ liệu từ jobs.csv
- Kiểm tra thông tin cơ bản (shape, dtypes, missing values)
- Thống kê mô tả ban đầu

**Bước 2:** Làm sạch dữ liệu trong `02_data_cleaning.ipynb`
- Xử lý giá trị thiếu
- Xử lý outliers
- Chuẩn hóa định dạng dữ liệu

**Bước 3:** Feature Engineering trong `03_feature_engineering.ipynb`
- Tạo biến salary_avg_vnd
- Chuyển đổi experience sang experience_years
- One-hot encoding cho các biến categorical
- Tạo các features mới từ skills, job_fields

**Bước 4:** Trực quan hóa trong `04_visualization.ipynb`
- Biểu đồ phân bổ việc làm theo thành phố
- Box plot phân bố lương theo các nhóm
- Word cloud cho skills
- Heatmap correlation matrix

**Bước 5:** Xây dựng mô hình trong `05_modeling.ipynb`
- Chia train/test set
- Thử nghiệm nhiều thuật toán
- Hyperparameter tuning
- Lưu mô hình tốt nhất

**Bước 6:** Đánh giá trong `06_evaluation.ipynb`
- Tính các metrics (MAE, RMSE, R²)
- Confusion matrix cho classification
- Feature importance analysis

### Giai đoạn 2: Chuyển code sang modules (src/)

**Mục đích:** Tổ chức lại code từ notebooks thành các module có thể tái sử dụng

#### File: `src/data/data_loader.py`
```python
import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def load_data(self):
        """Load dữ liệu từ CSV"""
        return pd.read_csv(self.filepath)
    
    def get_basic_info(self, df):
        """Lấy thông tin cơ bản về dataset"""
        info = {
            'shape': df.shape,
            'columns': df.columns.tolist(),
            'dtypes': df.dtypes.to_dict(),
            'missing': df.isnull().sum().to_dict()
        }
        return info
```

#### File: `src/data/data_cleaner.py`
```python
import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self):
        pass
    
    def handle_missing_values(self, df):
        """Xử lý giá trị thiếu"""
        # Logic xử lý từ notebook
        return df
    
    def remove_outliers(self, df, column, method='iqr'):
        """Loại bỏ outliers"""
        # Logic xử lý outliers
        return df
    
    def standardize_format(self, df):
        """Chuẩn hóa định dạng"""
        # Chuẩn hóa các cột
        return df
```

#### File: `src/features/feature_builder.py`
```python
class FeatureBuilder:
    def __init__(self):
        pass
    
    def create_salary_avg(self, df):
        """Tạo biến salary_avg_vnd"""
        df['salary_avg_vnd'] = (df['salary_min'] + df['salary_max']) / 2
        return df
    
    def convert_experience(self, df):
        """Chuyển đổi experience sang số năm"""
        # Logic chuyển đổi
        return df
    
    def encode_categorical(self, df, columns):
        """Mã hóa biến categorical"""
        # One-hot encoding hoặc label encoding
        return df
```

#### File: `src/models/predictor.py`
```python
import joblib
import numpy as np

class SalaryPredictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load('models/scaler.pkl')
    
    def preprocess_input(self, input_data):
        """Xử lý input trước khi dự đoán"""
        # Transform input data
        return processed_data
    
    def predict(self, input_data):
        """Dự đoán mức lương"""
        processed = self.preprocess_input(input_data)
        prediction = self.model.predict(processed)
        return prediction[0]
    
    def predict_with_confidence(self, input_data):
        """Dự đoán với khoảng tin cậy"""
        # Logic dự đoán kèm confidence interval
        return prediction, confidence_interval
```

### Giai đoạn 3: Xây dựng Flask Application

#### File: `run.py` (Entry point)
```python
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

#### File: `app/__init__.py`
```python
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here'
    
    CORS(app)
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app
```

#### File: `app/routes.py`
```python
from flask import Blueprint, render_template, request, jsonify
from src.models.predictor import SalaryPredictor

main = Blueprint('main', __name__)
predictor = SalaryPredictor('models/best_model.pkl')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        data = {
            'job_title': request.form['job_title'],
            'city': request.form['city'],
            'experience': request.form['experience'],
            'position_level': request.form['position_level'],
            'skills': request.form['skills'],
            'job_fields': request.form['job_fields']
        }
        
        # Dự đoán
        prediction = predictor.predict(data)
        
        return render_template('results.html', 
                             salary=prediction,
                             input_data=data)
    
    return render_template('predict.html')

@main.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint cho dự đoán"""
    data = request.get_json()
    prediction = predictor.predict(data)
    return jsonify({'predicted_salary': float(prediction)})
```

#### File: `app/templates/base.html`
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Dự Đoán Mức Lương{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav>
        <div class="container">
            <h1>Hệ Thống Dự Đoán Mức Lương</h1>
            <ul>
                <li><a href="{{ url_for('main.index') }}">Trang chủ</a></li>
                <li><a href="{{ url_for('main.predict') }}">Dự đoán</a></li>
            </ul>
        </div>
    </nav>
    
    <main class="container">
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2025 Salary Prediction System</p>
    </footer>
    
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
```

#### File: `app/templates/predict.html`
```html
{% extends "base.html" %}

{% block content %}
<div class="prediction-form">
    <h2>Nhập thông tin để dự đoán mức lương</h2>
    
    <form method="POST" action="{{ url_for('main.predict') }}">
        <div class="form-group">
            <label for="job_title">Chức danh công việc:</label>
            <input type="text" id="job_title" name="job_title" required>
        </div>
        
        <div class="form-group">
            <label for="city">Thành phố:</label>
            <select id="city" name="city" required>
                <option value="">Chọn thành phố</option>
                <option value="Hồ Chí Minh">Hồ Chí Minh</option>
                <option value="Hà Nội">Hà Nội</option>
                <option value="Đà Nẵng">Đà Nẵng</option>
                <!-- Thêm các option khác -->
            </select>
        </div>
        
        <div class="form-group">
            <label for="experience">Kinh nghiệm (năm):</label>
            <input type="number" id="experience" name="experience" min="0" required>
        </div>
        
        <div class="form-group">
            <label for="position_level">Cấp bậc:</label>
            <select id="position_level" name="position_level" required>
                <option value="">Chọn cấp bậc</option>
                <option value="Nhân viên">Nhân viên</option>
                <option value="Trưởng nhóm">Trưởng nhóm</option>
                <option value="Quản lý">Quản lý</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="skills">Kỹ năng (phân cách bằng dấu phẩy):</label>
            <input type="text" id="skills" name="skills" placeholder="Python, Data Analysis, SQL">
        </div>
        
        <div class="form-group">
            <label for="job_fields">Lĩnh vực:</label>
            <input type="text" id="job_fields" name="job_fields" placeholder="IT, Software">
        </div>
        
        <button type="submit" class="btn-predict">Dự đoán mức lương</button>
    </form>
</div>
{% endblock %}
```

## 4. WORKFLOW THỰC HIỆN

### Tuần 1-2: Phân tích dữ liệu
1. Hoàn thành các notebook từ 01 đến 04
2. Hiểu rõ dữ liệu và các pattern
3. Tạo các visualization cần thiết

### Tuần 3-4: Xây dựng mô hình
1. Thử nghiệm nhiều thuật toán trong notebook 05
2. So sánh và chọn mô hình tốt nhất
3. Lưu mô hình và các artifacts

### Tuần 5: Tổ chức code
1. Chuyển code từ notebooks sang src/
2. Tạo các module có thể tái sử dụng
3. Viết unit tests

### Tuần 6: Xây dựng Flask app
1. Tạo cấu trúc Flask application
2. Tích hợp mô hình vào routes
3. Thiết kế giao diện người dùng

### Tuần 7: Testing và deployment
1. Test toàn bộ hệ thống
2. Viết documentation
3. Chuẩn bị deploy lên server

## 5. LƯU Ý QUAN TRỌNG

### Best Practices

**Quản lý version:**
- Sử dụng Git để version control
- Commit thường xuyên với message rõ ràng
- Tạo branches cho các features mới

**Quản lý dependencies:**
- Cập nhật requirements.txt thường xuyên
- Pin version cho các thư viện quan trọng

**Code quality:**
- Follow PEP 8 style guide
- Viết docstrings cho functions và classes
- Comment code phức tạp

**Security:**
- Không commit API keys, secrets vào Git
- Sử dụng environment variables
- Validate user input trong Flask app

**Performance:**
- Cache model predictions nếu có thể
- Optimize data loading
- Sử dụng async cho I/O operations nếu cần

## 6. CÔNG CỤ HỖ TRỢ

**Development:**
- **Git** - Version control
- **Docker** - Containerization (optional)
- **Postman** - Test API endpoints

**Monitoring:**
- **Flask-DebugToolbar** - Debug trong development
- **Logging** - Track errors và performance

**Deployment:**
- **Gunicorn** - WSGI server cho production
- **Nginx** - Reverse proxy
- **Heroku/AWS/DigitalOcean** - Hosting platforms

## 7. NEXT STEPS

Sau khi hoàn thành cấu trúc cơ bản:

1. **Tối ưu hóa mô hình:** Tiếp tục cải thiện độ chính xác
2. **Mở rộng features:** Thêm visualizations, reports
3. **API Documentation:** Tạo Swagger/OpenAPI docs
4. **Mobile app:** Phát triển mobile interface
5. **Real-time updates:** Tích hợp real-time salary data
6. **User accounts:** Thêm authentication và personalization# salary-prediction-project
