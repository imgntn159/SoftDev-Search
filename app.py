from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route("/")
@app.route("/home", methods = ["POST"])
def home():
    return render_template("home.html")

@app.route("/results", methods = ["POST"])
def results():
    answer = str(request.form["search"])
    return render_template("results.html", answer = answer)

if __name__ == "__main__":
    app.debug = True
    app.run()
    
