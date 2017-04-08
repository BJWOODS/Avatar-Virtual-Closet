from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def lionel(): 
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()