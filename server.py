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
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/user')

@app.route('/user/show/<int:id>')
def show(id):
    data = {
        'id' : id
    }
    user=User.get_one(data)
    return render_template('show.html', user=user)

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        'id':id
    }
    user=User.get_one(data)
    return render_template('edit.html', user=user)

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/user')

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    User.delete(data)
    return redirect('/user')

if __name__ == "__main__":
    app.run(debug=True)