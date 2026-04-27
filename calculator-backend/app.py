from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        result = safe_eval(expression)
        return jsonify({'success': True, 'result': result, 'expression': expression})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

def safe_eval(expression):
    allowed_chars = set('0123456789+-*/().% ')
    if not all(char in allowed_chars for char in expression):
        raise ValueError('Invalid expression')
    return eval(expression)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
