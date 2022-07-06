from flask import Flask, make_response, redirect, abort
app = Flask(__name__)

#@app.route('/')
#def index():
#    return redirect('http://www.example.com')

    #response = make_response('<h1>This document carries a cookie!</h1>')
    #response.set_cookie('answer','42')
    #return response

    # return '<h1>Bad Request</h1>', 400
    #return '<h1>Hello Word!</h1>'

#@app.route('/user/<id>')
#def get_user(id):
#    user = 
#    if not user:
#        abort(404)
#    return '<h1>Hello, %s!</h1>' % user.name

if __name__ == '__main__':
    app.run(debug=True)
