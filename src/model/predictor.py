import pandas as pd
import numpy as np
import joblib
import json
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent))
from src.utils.config import (
    BEST_MODEL_PATH, SCALER_PATH, FEATURES_LIST_PATH, MODEL_INFO_PATH,
    EXPERIENCE_MAPPING, POSITION_ORDER, EXCHANGE_RATE
)

# Class để dự đoán mức lương dựa trên thông tin công việc
class SalaryPredictor:
    # Khởi tạo SalaryPredictor
    def __init__(self, model_path=None, scaler_path=None, features_path=None):

        self.model_path = model_path or BEST_MODEL_PATH
        self.scaler_path = scaler_path or SCALER_PATH
        self.features_path = features_path or FEATURES_LIST_PATH
        
        self.model = None
        self.scaler = None
        self.features_list = None
        self.model_info = None
        
        self._load_model()
        self._load_scaler()
        self._load_features()
        self._load_model_info()
    
    # Load mô hình từ file
    def _load_model(self):
        try:
            self.model = joblib.load(self.model_path)
            print(f"Model loaded from: {self.model_path}")
        except FileNotFoundError:
            print(f"Model file not found: {self.model_path}")
            raise
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            raise
    
    # Load scaler từ file
    def _load_scaler(self):
        try:
            self.scaler = joblib.load(self.scaler_path)
            print(f"Scaler loaded from: {self.scaler_path}")
        except FileNotFoundError:
            print(f"Scaler file not found: {self.scaler_path}")
            # Scaler có thể không bắt buộc
            self.scaler = None
        except Exception as e:
            print(f"Error loading scaler: {str(e)}")
            self.scaler = None
    
    # Load danh sách features từ file
    def _load_features(self):
        try:
            with open(self.features_path, 'r') as f:
                self.features_list = json.load(f)
            print(f"Features list loaded: {len(self.features_list)} features")
        except FileNotFoundError:
            print(f"Features file not found: {self.features_path}")
            raise
        except Exception as e:
            print(f"Error loading features: {str(e)}")
            raise
    # Load thông tin mô hình từ file
    def _load_model_info(self):
        try:
            with open(MODEL_INFO_PATH, 'r') as f:
                self.model_info = json.load(f)
            print(f"Model info loaded")
        except:
            self.model_info = {}
    # Xử lý input data thành định dạng phù hợp cho mô hình
    def preprocess_input(self, input_data):
        # Tạo DataFrame rỗng với tất cả features
        features_df = pd.DataFrame(0, index=[0], columns=self.features_list)
        
        # 1. Experience years
        if 'experience' in input_data:
            exp = input_data['experience']
            if isinstance(exp, str):
                features_df['experience_years'] = EXPERIENCE_MAPPING.get(exp, 0)
            else:
                features_df['experience_years'] = float(exp)
        
        # 2. Position level encoding
        if 'position_level' in input_data:
            pos = input_data['position_level']
            if pos in POSITION_ORDER:
                features_df['position_level_encoded'] = POSITION_ORDER.index(pos)
        
        # 3. Skills count và binary features
        if 'skills' in input_data:
            skills = str(input_data['skills']).split(',')
            skills = [s.strip().lower() for s in skills if s.strip()]
            features_df['skills_count'] = len(skills)
            
            # Set binary features cho skills
            for skill in skills:
                skill_col = f'has_skill_{skill.replace(" ", "_")}'
                if skill_col in self.features_list:
                    features_df[skill_col] = 1
        
        # 4. Job fields count và binary features
        if 'job_fields' in input_data:
            fields = str(input_data['job_fields']).split(',')
            fields = [f.strip().lower() for f in fields if f.strip()]
            features_df['fields_count'] = len(fields)
            
            # Set binary features cho fields
            for field in fields:
                field_col = f'field_{field.replace(" ", "_").replace("/", "_")}'
                if field_col in self.features_list:
                    features_df[field_col] = 1
        
        # 5. City binary features
        if 'city' in input_data:
            city = input_data['city']
            city_col = f'city_{city.lower().replace(" ", "_")}'
            if city_col in self.features_list:
                features_df[city_col] = 1
        
        # 6. Interaction features
        if 'exp_position_interaction' in self.features_list:
            features_df['exp_position_interaction'] = (
                features_df['experience_years'] * features_df['position_level_encoded']
            )
        
        if 'skills_exp_interaction' in self.features_list:
            features_df['skills_exp_interaction'] = (
                features_df['skills_count'] * features_df['experience_years']
            )
        
        # 7. Salary range features (nếu có trong input)
        if 'salary_min' in input_data and 'salary_max' in input_data:
            salary_min = float(input_data['salary_min'])
            salary_max = float(input_data['salary_max'])
            
            if 'salary_range' in self.features_list:
                features_df['salary_range'] = salary_max - salary_min
            
            if 'salary_range_ratio' in self.features_list:
                features_df['salary_range_ratio'] = (salary_max - salary_min) / (salary_min + 1)
        
        return features_df
    
    # Dự đoán mức lương
    def predict(self, input_data):

        # Preprocess input
        features_df = self.preprocess_input(input_data)
        
        # Predict
        prediction = self.model.predict(features_df)[0]
        
        return prediction
    
    # Dự đoán mức lương kèm thông tin chi tiết
    def predict_with_details(self, input_data):
        
        # Predict
        prediction = self.predict(input_data)
        
        # Lấy thông tin mô hình
        mae = self.model_info.get('test_mae', 0)
        r2 = self.model_info.get('test_r2', 0)
        
        # Tính khoảng tin cậy (dựa trên MAE)
        confidence_interval = (
            max(0, prediction - mae),
            prediction + mae
        )
        
        # Phân loại mức lương (Triệu VND)
        if prediction < 10: 
            category = 'Thấp'
        elif prediction < 20:
            category = 'Trung bình thấp'
        elif prediction < 30:
            category = 'Trung bình cao'
        else:
            category = 'Cao'
        
        result = {
            'predicted_salary': prediction,
            'predicted_salary_formatted': f'{prediction:,.0f}tr VND',
            'confidence_interval': {
                'lower': confidence_interval[0],
                'upper': confidence_interval[1],
                'lower_formatted': f'{confidence_interval[0]:,.0f}tr VND',
                'upper_formatted': f'{confidence_interval[1]:,.0f}tr VND'
            },
            'salary_category': category,
            'model_info': {
                'mae': mae,
                'r2': r2,
                'model_type': self.model_info.get('model_type', 'RandomForest')
            },
            'input_summary': {
                'experience_years': input_data.get('experience', 'N/A'),
                'position': input_data.get('position_level', 'N/A'),
                'city': input_data.get('city', 'N/A'),
                'skills_count': len(str(input_data.get('skills', '')).split(','))
            }
        }
        
        return result
    
    # Dự đoán cho nhiều inputs cùng lúc
    def predict_batch(self, input_list):

        predictions = []
        for input_data in input_list:
            pred = self.predict(input_data)
            predictions.append(pred)
        
        return predictions
    
    # Trả về thông tin về mô hình
    def get_model_info(self):
        return {
            'model_type': self.model_info.get('model_type', 'N/A'),
            'n_features': len(self.features_list),
            'test_mae': self.model_info.get('test_mae', 'N/A'),
            'test_rmse': self.model_info.get('test_rmse', 'N/A'),
            'test_r2': self.model_info.get('test_r2', 'N/A'),
            'best_params': self.model_info.get('best_params', {})
        }


# Hàm tiện ích để dự đoán nhanh mức lương
def predict_salary(job_title, city, experience, position_level, skills, job_fields):

    predictor = SalaryPredictor()
    
    input_data = {
        'job_title': job_title,
        'city': city,
        'experience': experience,
        'position_level': position_level,
        'skills': skills,
        'job_fields': job_fields
    }
    
    return predictor.predict_with_details(input_data)


if __name__ == '__main__':
    # Test SalaryPredictor
    print("="*70)
    print("Testing SalaryPredictor")
    print("="*70)
    
    try:
        # Khởi tạo predictor
        predictor = SalaryPredictor()
        
        # Test input
        test_input = {
            'job_title': 'Data Analyst',
            'city': 'Hồ Chí Minh',
            'experience': '2-5 năm',
            'position_level': 'Nhân viên',
            'skills': 'Python, SQL, Excel',
            'job_fields': 'IT, Data Analysis'
        }
        
        print("\n1. Test input:")
        for key, value in test_input.items():
            print(f"   {key}: {value}")
        
        print("\n2. Predicting...")
        result = predictor.predict_with_details(test_input)
        
        print("\n3. Prediction result:")
        print(f"   Predicted Salary: {result['predicted_salary_formatted']}")
        print(f"   Confidence Interval: {result['confidence_interval']['lower_formatted']} - {result['confidence_interval']['upper_formatted']}")
        print(f"   Category: {result['salary_category']}")
        
        print("\n4. Model info:")
        model_info = predictor.get_model_info()
        for key, value in model_info.items():
            print(f"   {key}: {value}")
        
        print("\n" + "="*70)
        print("SalaryPredictor test completed successfully!")
        print("="*70)
        
    except Exception as e:
        print(f"\nError during testing: {str(e)}")
        import traceback
        traceback.print_exc()