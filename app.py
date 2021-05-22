from flask import FlaskProject, redirect, url_for
from flask import render_template


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


if __name__ == '__main__':
    app.run(debug=True)
