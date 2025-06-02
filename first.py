from flask import Flask,request
first=Flask(__name__)#object banaya app naam ka aur ye object humari website ko represent krega
@first.route('/')
def home():
    return 'Hello User ! This is my first Flask App'
@first.route("/about")
def about():
    return 'This is about us page'
@first.route("/contact")
def contact():
    return "This is a contact us page"
@first.route('/submit',methods=["GET","POST"])
def submit():
    if request.method=="POST":
        return "You send data!"
    else:
        return "You are only viewing the form!"
