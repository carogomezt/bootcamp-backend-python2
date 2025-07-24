# import the Flask class from the flask module
from functools import wraps

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

# create the application object
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            print("User is logged in")
            return f(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for("login"))

    return wrap


# use decorators to link the function to a url
@app.route("/")
@login_required
def home():
    # return "Hello, World!"  # return a string
    return render_template("index.html")  # render a template


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")  # render a template


# Route for handling the login page logic
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if (
            request.form["username"] != "admin"
            or request.form["password"] != "admin"
        ):
            error = "Invalid Credentials. Please try again."
        else:
            session["logged_in"] = True
            flash("You were logged in.")
            return redirect(url_for("home"))
    return render_template("login.html", error=error)


@app.route("/logout")
@login_required
def logout():
    session.pop("logged_in", None)
    flash("You were logged out.")
    return redirect(url_for("home"))


# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(debug=True)
