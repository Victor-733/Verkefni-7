import pymysql
from bottle import *
from sys import argv

# Static
@route("/static/<skra>")
def static_skrar(skra):
    return static_file(skra, root="./static/")

# run
run(app=app, host="0.0.0.0", port=argv[1], debug=True)

# Connection
conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1611012220', passwd='mypassword')