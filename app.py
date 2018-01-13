from flask import Flask
from flask import render_template
from flask import Response
from flask import send_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')


if __name__=='__main__':
    app.run(debug=True)