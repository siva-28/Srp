from flask import Flask,flash,redirect,render_template,request,session,abort

app = Flask(__name__)


@app.route("/members")
def members():
    return "Members"


@app.route("/members/<string:name>/")
def index(name):
    return render_template('home.html',**locals())


if __name__=="__main__":
    app.run(host='127.0.0.1', port=80)
