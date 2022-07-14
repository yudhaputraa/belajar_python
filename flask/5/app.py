from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    variabel1 = 9
    variabel2 = 'flask'
    variabel3 = 123.456
    return render_template('index.html', var1=variabel1, var2=variabel2, var3=variabel3)

if __name__ == '__main__':
    app.run(debug=True)