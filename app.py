import pymysql
from bottle import *
from sys import argv

@route('/')
def index()
    return template('index')

@route('/donyskra', method='POST')
def nyr():
    u = request.forms.get('user')
    p = request.forms.get('pass')
    n = request.forms.get('nafn')

# Connection
conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1611012220', passwd='mypassword', db='1611012220_Verkefni_7')

# Static
@route("/static/<skra>")
def static_skrar(skra):
    return static_file(skra, root="./static/")

# run
run(app=app, host="0.0.0.0", port=argv[1], debug=True)