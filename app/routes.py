from flask import Blueprint, render_template, request, jsonify
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from src.model.predictor import SalaryPredictor

# Tạo blueprint
main = Blueprint('main', __name__)

# Khởi tạo predictor (global)
try:
    predictor = SalaryPredictor()
    print("Predictor loaded successfully in routes")
except Exception as e:
    print(f"Error loading predictor: {str(e)}")
    predictor = None

# Trang chủ
@main.route('/')
def index():
    return render_template('index.html')

# Trang dự đoán lương
@main.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Lấy dữ liệu từ form
            input_data = {
                'job_title': request.form.get('job_title', ''),
                'city': request.form.get('city', ''),
                'experience': request.form.get('experience', ''),
                'position_level': request.form.get('position_level', ''),
                'skills': request.form.get('skills', ''),
                'job_fields': request.form.get('job_fields', '')
            }
            
            # Validate input
            if not all([input_data['job_title'], input_data['city'], 
                       input_data['experience'], input_data['position_level']]):
                return render_template('predict.html', 
                                     error="Vui lòng điền đầy đủ thông tin bắt buộc!")
            
            # Dự đoán
            if predictor is None:
                return render_template('predict.html',
                                     error="Hệ thống chưa sẵn sàng. Vui lòng thử lại sau!")
            
            result = predictor.predict_with_details(input_data)
            
            # Render kết quả
            return render_template('results.html',
                                 result=result,
                                 input_data=input_data)
        
        except Exception as e:
            return render_template('predict.html',
                                 error=f"Lỗi khi dự đoán: {str(e)}")
    
    # GET request - hiển thị form
    return render_template('predict.html')

# API endpoint để dự đoán lương (JSON)
@main.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        # Lấy data từ request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'error': 'Không có dữ liệu'
            }), 400
        
        # Validate required fields
        required_fields = ['job_title', 'city', 'experience', 'position_level']
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            return jsonify({
                'error': f'Thiếu dữ liệu bắc buộc: {", ".join(missing_fields)}'
            }), 400
        
        # Dự đoán
        if predictor is None:
            return jsonify({
                'error': 'Lỗi dữ đoán không thành công'
            }), 500
        
        result = predictor.predict_with_details(data)
        
        return jsonify({
            'success': True,
            'data': result
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# API endpoint để lấy thông tin về mô hình
@main.route('/api/model-info', methods=['GET'])
def api_model_info():

    try:
        if predictor is None:
            return jsonify({
                'error': 'Lỗi dữ đoán không thành công'
            }), 500
        
        info = predictor.get_model_info()
        
        return jsonify({
            'success': True,
            'data': info
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

#  Trang giới thiệu
@main.route('/about')
def about():
    return render_template('about.html')

# Trang tài liệu
@main.route('/documentation')
def documentation():
    return render_template('documentation.html')


#  Health check cho deployment
@main.route('/health')
def health():
    status = 'healthy' if predictor is not None else 'unhealthy'
    return jsonify({
        'status': status,
        'predictor_loaded': predictor is not None
    }), 200 if predictor else 500