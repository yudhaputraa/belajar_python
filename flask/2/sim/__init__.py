from flask import Flask, Blueprint

app = Flask('__name__', template_folder='sim/templates', static_folder='sim/static')
app.config['SECRET_KEY'] = "gamariamandar"

from sim.mahasiswa.routes import rmahasiswa
app.register_blueprint(rmahasiswa)