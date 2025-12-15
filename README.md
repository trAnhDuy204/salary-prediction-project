# 💼 Hệ Thống Dự Đoán Mức Lương - Salary Prediction System

Dự án Machine Learning dự đoán mức lương dựa trên thông tin công việc, kinh nghiệm và kỹ năng.

## 🎯 Tính Năng

- ✅ Dự đoán mức lương chính xác với Random Forest Model
- ✅ Khoảng tin cậy cho mỗi dự đoán
- ✅ Giao diện web thân thiện với Flask
- ✅ RESTful API để tích hợp
- ✅ Phân tích dữ liệu toàn diện với Jupyter Notebooks
- ✅ 85,000+ tin tuyển dụng từ thị trường Việt Nam

## 📊 Hiệu Suất Mô Hình

- **R² Score**: ~0.80-0.85
- **MAE**: ~2-3 triệu VND
- **Model**: Random Forest (Optimized)
- **Features**: 50+ features

## 🛠️ Công Nghệ Sử Dụng

### Backend
- Python 3.9+
- Flask 3.0
- Scikit-learn
- Pandas & NumPy

### Frontend
- Bootstrap 5
- Font Awesome
- Custom CSS/JS

### Machine Learning
- Random Forest Regressor
- Feature Engineering
- Cross-validation
- Hyperparameter Tuning

## 📁 Cấu Trúc Dự Án

```
salary-prediction-project/
├── data/
│   ├── raw/                    # Dữ liệu gốc
│   └── processed/              # Dữ liệu đã xử lý
├── notebooks/                  # Jupyter notebooks (01-06)
│   └── figures/               # Biểu đồ
├── src/                        # Source code modules
│   ├── data/                  # Data processing
│   ├── features/              # Feature engineering
│   ├── models/                # ML models
│   ├── visualization/         # Plotting
│   └── utils/                 # Utilities
├── models/                     # Trained models
├── app/                        # Flask application
│   ├── templates/             # HTML templates
│   ├── static/                # CSS, JS, images
│   └── routes.py              # Routes
├── tests/                      # Unit tests
├── requirements.txt
├── run.py                      # Entry point
└── README.md
```

## 🚀 Cài Đặt và Chạy

### 1. Clone Repository

```bash
git clone https://github.com/your-username/salary-prediction.git
cd salary-prediction
```

### 2. Tạo Môi Trường Ảo

```bash
# Sử dụng venv
python -m venv venv

# Kích hoạt môi trường
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Cài Đặt Dependencies

```bash
pip install -r requirements.txt
```

### 4. Chuẩn Bị Dữ Liệu

- Đặt file `jobs.csv` vào thư mục `data/raw/`
- Chạy các notebooks từ 01 đến 06 để xử lý dữ liệu và train model

### 5. Chạy Ứng Dụng Flask

```bash
python run.py
```

Truy cập: `http://localhost:5000`

## 📓 Hướng Dẫn Sử Dụng Notebooks

### Chạy Lần Lượt:

1. **01_data_exploration.ipynb** - Khám phá dữ liệu
2. **02_data_cleaning.ipynb** - Làm sạch dữ liệu
3. **03_feature_engineering.ipynb** - Tạo features
4. **04_visualization.ipynb** - Trực quan hóa
5. **05_modeling.ipynb** - Xây dựng mô hình
6. **06_evaluation.ipynb** - Đánh giá và phân tích

### Output:
- Dữ liệu processed trong `data/processed/`
- Model trained trong `models/`
- 20+ biểu đồ trong `notebooks/figures/`

## 🌐 API Endpoints

### POST /api/predict
Dự đoán mức lương

**Request Body:**
```json
{
  "job_title": "Data Analyst",
  "city": "Hồ Chí Minh",
  "experience": "2-5 năm",
  "position_level": "Nhân viên",
  "skills": "Python, SQL, Excel",
  "job_fields": "IT, Data Analysis"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "predicted_salary": 15000000,
    "confidence_interval": {
      "lower": 12000000,
      "upper": 18000000
    },
    "salary_category": "Trung bình cao"
  }
}
```

### GET /api/model-info
Lấy thông tin mô hình

### GET /health
Health check

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_predictor.py

# Run with coverage
pytest --cov=src tests/
```

## 📦 Deployment

### Option 1: Heroku

```bash
# Login
heroku login

# Create app
heroku create salary-predictor-app

# Deploy
git push heroku main

# Open app
heroku open
```

### Option 2: Docker

```bash
# Build image
docker build -t salary-predictor .

# Run container
docker run -p 5000:5000 salary-predictor
```

### Option 3: Railway/Render

- Push code lên GitHub
- Connect repository với Railway/Render
- Set environment variables
- Deploy tự động

## ⚙️ Configuration

Chỉnh sửa `src/utils/config.py`:

```python
# Flask settings
FLASK_PORT = 5000
FLASK_DEBUG = True

# Model parameters
EXCHANGE_RATE = 24000  # USD to VND
IQR_FACTOR = 3.0

# Features
N_TOP_SKILLS = 10
N_TOP_FIELDS = 10
```

## 📈 Kết Quả

### Model Performance:
- Cross-validation MAE: ~2.5M VND
- Test R² Score: 0.82
- 80%+ predictions có sai số <20%

### Key Insights:
- Kinh nghiệm là yếu tố quan trọng nhất (35% importance)
- Vị trí địa lý ảnh hưởng 20% đến lương
- Top skills: Python, Java, English có mức lương cao
- TP.HCM và Hà Nội có mức lương cao nhất

## 🤝 Đóng Góp

Contributions are welcome! Please:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see LICENSE file.

## 👥 Authors

- **Your Name** - *Initial work*

## 🙏 Acknowledgments

- Dataset from Vietnamese job market
- Inspired by Kaggle competitions
- Built with ❤️ for learning

## 📞 Contact

- Email: your.email@example.com
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [Your Name](https://linkedin.com/in/your-profile)

---

⭐ **Star this repo if you find it helpful!**