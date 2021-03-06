from flask import Flask, render_template, request, session
import os

app = Flask (__name__)  
app.secret_key = os.urandom(32)

username = "bob"
password = "bobbins"

@app.route("/",methods=['POST','GET'])
def hello_world():
    '''
    checks user info and displays greet or login

    returns html page greet or login 
    '''
    print "\n\n"
    print "Cookie username: ", session.get('username')
    print "Cookie password: ",session.get('password')
    if session.get('username') == username and session.get('password') == password:
        return render_template('greet.html',user=session.get('username'))
    else:
        return render_template( 'login.html' )

@app.route("/greet",methods=['POST','GET'])
def greet():
    '''
    sets user info keys

    returns greet or error html pages 
    '''
    print "\n\n"
    print "Form username: ", request.form.get('username')
    print "Form password: ", request.form.get('password')
    session['username'] = request.form.get('username')
    session['password'] = request.form.get('password')
    if session.get('username')== username and session.get('password')==password:
        return render_template( 'greet.html', user = session.get('username') )
    elif session.get('username') != username:
        return render_template('error.html', error = "Username incorrect!")
    else:
        return render_template('error.html', error = "Password incorrect!")

@app.route("/logout",methods=['POST','GET'])
def logout():
    '''
    clears cookies

    returns login html page
    '''
    session.pop("username")
    session.pop("password")
    return render_template('login.html')

if __name__ == "__main__":
    app.debug = True;
    app.run()
