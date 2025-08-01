# app.py
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

### pip install flask , flask_cors



app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')  # templates/index.html を表示

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    text = data.get('text', '')
    result = len(text)  # 例：文字数を返す
    return jsonify({'length': result})

if __name__ == '__main__':
    app.run(debug=True)