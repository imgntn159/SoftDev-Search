from flask import Flask, render_template, request, redirect, url_for
import google, bs4, re, urllib2


app = Flask(__name__)

@app.route("/")
@app.route("/home", methods = ["POST"])
def home():
    return render_template("home.html")

@app.route("/results", methods = ["POST"])
def results():
    answer = str(request.form["search"])
    
    pages = google.search(answer,num=10,start=0,stop=10)
    plist = []
    for r in pages:
        page = (urllib2.urlopen(r).read().decode('ascii'))
        plist.append(bs4.BeautifulSoup(page).get_text(page))
    #Each item in plist contains the raw text, partly taken by classcode
    
    pstr = '' 
    for p in plist:
        pstr+=p
        pstr+=' '
    #A string centipede of the raw texts with spaces inbetween for the regex function
    
    pattern = '[A-Z]\w+\s+[A-Z]\w+'
    #Here we'd add a regex/algorithm to look for whatever
    
    names = re.findall(pattern, pstr)

    d = {'Not Found': 0}
    for name in names:
        if name in d:
            d['name'] += 1
        else:
            d['name'] = 1
    finalAns = ''
    finalNum = 0
    for n in d:
        if d[n] > finalNum:
            finalNum = d[n]
            finalAns = n
    
    
    return render_template("results.html", answer = finalAns)

if __name__ == "__main__":
    app.debug = True
    app.run()
    #host='0.0.0.0', port=8080
    
