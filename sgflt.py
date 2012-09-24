from flask import *

app = Flask(__name__)
app.config.from_pyfile('sgflt.cfg', silent=True)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')

