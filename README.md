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
