import pymysql
from bottle import *
from sys import argv
from beaker.middleware import SessionMiddleware

session_opts = {
    "session.type": "file",
    "session.data_dir": "./data",
    "session.cookie_expires": 600,
    "session.auto": True
}
app = SessionMiddleware(app(), session_opts)

@route('/')
def index():
    return template('index')

# -------- SKRA INN --------- #

@route('/donyskra', method='POST')
def nyr():
    u = request.forms.get('user')
    p = request.forms.get('pass')
    n = request.forms.get('nafn')

    # Connection
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1611012220', passwd='mypassword', db='1611012220_Verkefni_7')

    #cursor
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM users where user=%s", (u))
    result = cur.fetchone()

    if result[0] == 0:
        cur.execute("INSERT INTO users VALUES(%s, %s, %s)", (u, p, n))
        conn.commit()
        cur.close()
        conn.close()
        return u, " hefur verið skráður <br><a href='/'>Heim</a>"
    else:
        return u, " er frátekið notendanafn, reyndu aftur <br><a href='/#ny'>Nýskrá</a>"
# --------- INNSKRA ---------- #

@route('/doinnskra', method='POST')
def doinn():
    u = request.forms.get('user')
    p = request.forms.get('pass')

    # Connection
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1611012220', passwd='mypassword', db='1611012220_Verkefni_7')
    # cursor
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM users where user=%s and pass=%s",(u,p))
    result = cur.fetchone()

    print(result)
    if result[0] == 1:
        cur.close()
        conn.close()
        return template('leyni', u=u)
    else:
        return template('ekkileyni')

# ------------------------------------------------------------#
@route('/members')
def member():
    conn = pymysql.connect(host="tsuts.tskoli.is", port=3306, user='1611012220', passwd='mypassword', db='1611012220_Verkefni_7')
    c = conn.cursor()
    c.execute("SELECT nafn FROM users")
    result = c.fetchall()
    c.close()
    output = template('members', rows=result)
    return output
###############################################################

# Static
@route("/static/<skra>")
def static_skrar(skra):
    return static_file(skra, root="./static/")

# run
try:
    run(host="0.0.0.0", port=os.environ.get('PORT'))
except:
    run(debug=True)