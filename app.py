from flask import Flask, render_template, request, jsonify
import languagemodels as lm

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        user_input = request.json['user-message']
        response = get_response(user_input)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)})

def get_response(user_input):
    res = lm.do(user_input)
    return res

if __name__ == '__main__':
    app.run(debug=True)
