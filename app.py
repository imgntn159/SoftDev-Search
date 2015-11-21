from flask import Flask, render_template, request, redirect, url_for
import google, bs4, re


app = Flask(__name__)

@app.route("/")
@app.route("/home", methods = ["POST"])
def home():
    return render_template("home.html")

@app.route("/results", methods = ["POST"])
def results():
    answer = str(request.form["search"])
    '''
    pages = google.search(answer,num=10,start=0,stop=10)
    plist = []
    for r in pages:
        page = (urllib2.urlopen(plist[8]).read().decode('ascii'))
        plist.append(bs4.BeautifulSoup(page).get_text(page))
        
    #Each item in plist contains raw text from the urls, taken from classcode
    #Here we'd add a regex/algorithm to look for whatever
    '''
    return render_template("results.html", answer = answer)

if __name__ == "__main__":
    app.debug = True
    app.run()
    
