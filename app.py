import config
import os
from flask import Flask

from dct.views import dct


app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
app.register_blueprint(dct)
 