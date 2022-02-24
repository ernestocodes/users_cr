from flask import Flask, render_template, redirect, request
from user import User
app=Flask(__name__)
@app.route('/user')
def read():
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)

@app.route('/user/new')
def new():
    return render_template('create.html')

@app.route('/user/create_user', methods=['POST'])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/user')

if __name__ == "__main__":
    app.run(debug=True)