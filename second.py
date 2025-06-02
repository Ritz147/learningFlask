from flask import Flask,request,redirect,url_for,session,Response
second=Flask(__name__)
second.secret_key="supersecret"
#homepage
@second.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if username=="admin" and password=="123":
            session["user"]=username#store in session
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials , Try again!",mimetype="text/plain")#flask by default text/HTML ko bhejta hai
    return f'''
           <h2>Login Page</h2>
           <form method="POST">
            Username:<input type="text" name="username"><br>
            Password:<input type="text" name="password"><br>
            <input type="submit" value="Login">
           </form>
           '''
#welcome page after login
@second.route("/welcome")
def welcome():
    if "user" in session :
        return f'''
        <h2>Welcome,{session["user"]}!</h2>
        <a href={url_for('logout')}>Logout</a>

    '''
    return redirect(url_for('login'))
#logout
@second.route("/logout")
def logout():
    session.pop("user",None)#if user not in session then none prevents us fromany error
    return redirect(url_for('login'))


