from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/submit')
def submit():
        return render_template('submit.html')