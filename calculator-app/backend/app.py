from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)  # 允許跨域請求

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        
        # 安全地計算表達式
        result = safe_eval(expression)
        
        return jsonify({
            'success': True,
            'result': result,
            'expression': expression
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

def safe_eval(expression):
    # 允許的字符
    allowed_chars = set('0123456789+-*/().% ')
    # 檢查是否只包含允許的字符
    if not all(char in allowed_chars for char in expression):
        raise ValueError('Invalid expression')
    # 使用 Python 的 eval 進行計算
    return eval(expression)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
