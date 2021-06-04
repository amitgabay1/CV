from flask import Flask, url_for, session
from flask import render_template, request , redirect


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



@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    name = 'NONE'
    Users = {"amit": "gabay", "ido": "gabay", "omer": "gabay", "lior": "ribak", "ariel": "amit"}
    username = ' '
    logged_in = True

    if request.method == 'GET':
        if 'name' in request.args:
            name = request.args['name']

    if request.method == 'POST':
        username = request.form['username']
        session['logged_in'] = True
        session['username'] = username


    return render_template('assignment9.html',
                           request_method=request.method,
                           name = name,
                           Users = Users,
                           username = username)

@app.route('/log_out')
def log_out():
    session.pop('username')
    session['logged_in'] = False
    return redirect('/assignment9')


if __name__ == '__main__':
    app.run()