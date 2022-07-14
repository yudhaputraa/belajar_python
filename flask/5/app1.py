from flask import Flask
from models import persegipanjang

app = Flask(__name__)

@app.route('/')
def index():
    obj = persegipanjang(10.0,8.0)
    return '''
    <h1>Hello Word</h1>
    
    luas persegi panjang = %.3f<br>
    Keliling persegi panjang = %.3f
    ''' % (obj.luas(), obj.keliling())

if __name__ == '__main__':
    app.run(debug=True, port=5050)