from flask import render_template
from uceasy import app


@app.route('/')
@app.route('/index')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')
