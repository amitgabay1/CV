from flask import Flask,url_for
from flask import render_template, request


app = Flask(__name__)

@app.route('/UserList')
def UserList():
    return render_template('UsersList.html')


@app.route('/Amit_Gabay-CV')
def page2():
    return render_template('Amit_Gabay-CV.html')


@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html', hobby2='Cooking', name="Amit", hobbies=['Running','Reading','Dancing'])

@app.route('/assignment8')
def assignment8_add():
    return render_template('assignment8_add.html', hobby2='Cooking', name="Amit", hobbies=['Running','Reading','Dancing'])



@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    username = ''
    if session['Logged_in']:
        username = session['username']
    users = [
        {'id': 1, 'firstName': "amit", 'lastName': "gabay", 'age': 25},
        {'id': 2, 'firstName': "ariel", 'lastName': "amit", 'age': 22},
        {'id': 3, 'firstName': "lior", 'lastName': "ribak", 'age': 25},
        {'id': 4, 'firstName': "gili ", 'lastName': "keren", 'age': 18},
        {'id': 5, 'firstName': "roni", 'lastName': "nadler", 'age': 20},
        {'id': 6, 'firstName': "may", 'lastName': "daniel", 'age': 22},
        {'id': 6, 'firstName': "noy", 'lastName': "kasher", 'age': 41},
    ]
    firstname = ''
    if request.method == 'GET':
        if 'firstname' in request.args:
            firstname = request.args['firstname']
    if request.method == 'POST':
        if request.form["btn"] == "log out":
            session['Logged_in'] = False
            session['username'] = ''
            username = ''
        else:
            username = request.form['username']
            session['Logged_in'] = True
            session['username'] = username
    return render_template('assignment9.html',
                           request_method=request.method, username=username,
                           firstname=firstname, users=users)
if __name__ == '__main__':
    app.run(debug=True)