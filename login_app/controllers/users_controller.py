from flask import render_template, request, redirect, session
from login_app import app
from login_app.models.User import User
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)

@app.route( "/" ) #redirect allway to home
def displayLoginWall():
    print("ROUTE /, displayLoginWall in excecution*****************")
    return redirect ('/login')

@app.route( "/login", methods = ['GET'] )#Home page
def displayLoginRegistration():
    print("ROUTE /login, displayLoginRegistration in excecution*****************")
    return render_template( "loginwall.html")

@app.route('/login/register', methods = ['POST'] )#receive the data an does the registration
def registerUser():
    print("ROUTE /login/register, registerUser ==> ( ['POST'] ) in excecution*****************")
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    users_password = request.form['users_password']
    encryptedpassword = bcrypt.generate_password_hash(users_password)
    confirm_users_password = request.form['confirm_users_password']

    data = (first_name,last_name,email,users_password,encryptedpassword,confirm_users_password)
    print("FROM FORM 1 REGISTER: ", data )
    print("END OF REGISTER PART++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", data)
    if User.validate_registration(data):
        User.register_login(data)
    else:
        print("invalid values")
    return redirect('/login')


@app.route('/login/user', methods = ['POST'] )#receive the data from DB and redirects to the private wall
def userlogin():
    print("ROUTE /login/user, userlogin ==> ( ['POST'] ) in excecution*****************")
    email = request.form['email']
    users_password = request.form['users_password']

    data = (email, users_password)
    print("FROM FORM 2 LOGIN: ", data )
    result  = User.user_login(data)
    print("END OF LOGIN PART++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", data)
    print("Result: ", result)

    if len( result ) > 0:
        encryptedPassword = result[0]['users_password']
        print(encryptedPassword)
        if bcrypt.check_password_hash( encryptedPassword, users_password ):
            session.clear()
            users_id = result[0]['users_id']
            session['users_id'] = users_id
            return redirect ('/wall')
        else:
            messageWrongPass = "Wrong credentials provided."
            session['ErrorMessage'] = messageWrongPass
    else:
        messageWrongPass = "There is no user with this information"
        session['ErrorMessage'] = messageWrongPass
    return redirect('/login')

@app.route( "/wall", methods = ['GET'] )
def privateWall():
    print("ROUTE /wall, privateWall in excecution*****************")
    if 'users_id' not in session:
        return redirect('/logout')
    data ={
        'users_id': session['users_id']
    }
    users = User.get_userBy_id(data)
    return render_template( "privatewall.html", users = users)

@app.route('/logout')
def userlogout():
    session.clear()
    return redirect('/')




# #//////////////////////////////////////// EDIT PART ///////////////////////////////////////////
# #Here we're trying to redirect to the next page
# @app.route('/users/edit/<id>')
# def showUsersData(id):
#     updatedUsersInTable = User.get_one(id)
#     print("EditUserData: ", updatedUsersInTable)
#     return render_template("edit.html", users1 = updatedUsersInTable, id = id)

# #We're trying to got a form here
# @app.route('/users/show/<id>', methods=['POST'])
# def gotAndEditForm(id):
#     data = {
#         "first_name2Fromform2" : request.form['first_name2'],
#         "lastst_name2Fromform2" : request.form['last_name2'],
#         "email2Fromform2" : request.form['email2'],
#         "id" : id
#     }
#     edited = User.editUserData(data)
#     result = User.get_one(id)
#     print("EditUserData: ", result)
#     return render_template ("show.html", users1 = result, id = id, edited = edited )

# @app.route('/users/data/<id>')
# def showUsersDataInShowPage(id):
#     user = User.get_one(id)
#     print("1 :", user)
#     updatedUsersInTable = User.get_one(id)
#     print("EditUserData: ", updatedUsersInTable)
#     return render_template("show.html", users1 = updatedUsersInTable, id = id)

# @app.route("/users/delete/<id>")
# def deleteThisUser(id):
#     data={
#         'id': id
#     }
#     result2 = User.deleteUser(data)
#     print("EditUserData: ", result2)
#     return redirect('/users')
