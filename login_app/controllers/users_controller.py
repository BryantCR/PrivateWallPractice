from flask import render_template, request, redirect
from login_app import app
from login_app.models.User import User

@app.route( "/" )
def displayLogin():
    return redirect ('/users')

@app.route( "/users" )
def displayAllUsers():
    currentUsersInTable = User.get_all_users()
    print(currentUsersInTable)
    return render_template( "read.html", users1 = currentUsersInTable)

@app.route('/users/new')
def goToCreate():
    return render_template( "create.html")

@app.route('/users/create', methods=['POST'])
def create():
    print(request.form)
    User.addDataForm(request.form)
    return redirect('/users')

#//////////////////////////////////////// EDIT PART ///////////////////////////////////////////
#Here we're trying to redirect to the next page
@app.route('/users/edit/<id>')
def showUsersData(id):
    updatedUsersInTable = User.get_one(id)
    print("EditUserData: ", updatedUsersInTable)
    return render_template("edit.html", users1 = updatedUsersInTable, id = id)

#We're trying to got a form here
@app.route('/users/show/<id>', methods=['POST'])
def gotAndEditForm(id):
    data = {
        "first_name2Fromform2" : request.form['first_name2'],
        "lastst_name2Fromform2" : request.form['last_name2'],
        "email2Fromform2" : request.form['email2'],
        "id" : id
    }
    edited = User.editUserData(data)
    result = User.get_one(id)
    print("EditUserData: ", result)
    return render_template ("show.html", users1 = result, id = id, edited = edited )

@app.route('/users/data/<id>')
def showUsersDataInShowPage(id):
    user = User.get_one(id)
    print("1 :", user)
    updatedUsersInTable = User.get_one(id)
    print("EditUserData: ", updatedUsersInTable)
    return render_template("show.html", users1 = updatedUsersInTable, id = id)

@app.route("/users/delete/<id>")
def deleteThisUser(id):
    data={
        'id': id
    }
    result2 = User.deleteUser(data)
    print("EditUserData: ", result2)
    return redirect('/users')
