from flask import *

#create the app#
app = Flask(__name__)
app.config.from_pyfile('sgflt.cfg', silent=True)

import sgflt.views

