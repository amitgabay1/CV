from flask import Flask, url_for, session
from flask import render_template, request


app = Flask(__name__,static_url_path='/static')

@app.route('/Amit_Gabay-CV.html')
@app.route('/')
def index():
    return render_template('Amit_Gabay-CV.html')

@app.route('/UserList.html')
def UserList():
    return render_template('/UserList.html')

@app.route('/assignment8.html')
def assignment8():
    return render_template('/assignment8.html',
    user = {'firstname': "amit", 'lastname': "gabay"},
    hobbies=['running','dancing','baking'])

@app.route('/assignment_add.html')
def assignment82():
    return render_template('/assignment_add.html',
    user = {'firstname': "amit", 'lastname': "gabay"},
    movies=['frind with benfit','bonnie and clayde','titanic'])


if __name__ == '__main__':
    app.run()