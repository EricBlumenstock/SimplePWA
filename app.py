from flask import Flask
from flask import render_template
from flask import send_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/sw.js', methods=['GET'])
def sw():
    return send_file('static/js/sw.js', mimetype='text/javascript')


if __name__=='__main__':
    app.run(debug=True)