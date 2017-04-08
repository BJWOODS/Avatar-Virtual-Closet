from flask import *
app = Flask(__name__)

#app.run(host='0.0.0.0')

@app.route('/')
def index():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()