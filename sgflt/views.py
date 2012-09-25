from flask import *
from sgflt import app

@app.route('/')
def index():
    return render_template('index.html')


