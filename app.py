from flask import Flask,render_template,request,flash,redirect,url_for,session
from user import UserOperation
from encryption import Encryption
from validate import myvalidate
from myemail import Email
from myrandom import randomnumber

app = Flask(__name__)
app.secret_key="df789iofd89ewoieh89re"

userobj = UserOperation()   # User object
validobj = myvalidate()  # validation object
emailobj = Email(app)  # Email object

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_signup',methods=['GET','POST'])
def user_signup():
    if request.method=='GET':
        return render_template('user_signup.html')
    else:
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        user_name=request.form['user_name']
        password=request.form['password']
        #--------------validation--------------
        frm=[fname,lname,email,user_name,password]
        if(not validobj.required(frm)):
            flash("field can not be empty!!")
            return redirect(url_for('user_signup'))
        #-----password encryption-----------
        e = Encryption()
        password=e.convert(password)
        #-----------------------------------
        r = userobj.user_check(user_name)
        rc = userobj.email_check(email)
        if(r==0 and rc==0):
            global otp
            otp = randomnumber()
            subject ="Cloud Beats Email Verification"
            msg = "Hi "+fname+"\nYour Email OTP is "+str(otp)+"\nThank You\nCloud Beats"
            emailobj.compose_mail(subject,email,msg)

            userobj.user_insert(fname,lname,email,user_name,password)
            flash("OTP Send to your registered Email!!")
            return redirect(url_for('otpverify',email=email))
        else:
            if(rc!=0):
                flash("Email already exist")
            elif(r!=0):
                flash("user name already exist")
            return redirect(url_for('user_signup'))

@app.route('/otpverify',methods=['GET','POST'])
def otpverify():
    if( 'otp' in globals()):
        if(request.method=='GET'):
            email = request.args.get('email')
            return render_template('otp.html',email=email)
        else:
            n1=request.form['n1']
            n2=request.form['n2']
            n3=request.form['n3']
            n4=request.form['n4']
            otpinput = n1+n2+n3+n4
            if(str(otp)==otpinput):
                flash("Successfully Registered...login now")
                return redirect(url_for('user_login'))
            else:
                email=request.form['email']
                userobj.user_delete(email)
                flash("Email Verification Failed... Register Again!!")
                return redirect(url_for('user_signup'))
    else:
        return "can't access this page"  


@app.route('/user_login',methods=['GET','POST'])
def user_login():
    if(request.method=='GET'):
        return render_template("user_login.html")
    else:
        user_name=request.form['user_name']
        password=request.form['password']

        # PASSWORD ENCRYPTION *****************
        e=Encryption()
        password=e.convert(password)

        # ***********************
        r=userobj.user_login(user_name,password)
        if(r==0):
            flash("invalid credentials!!")
            return redirect(url_for("user_login"))
        else:
            # return "welcome "+ session["user_fname"]
            return redirect(url_for("user_dashboard"))
        
@app.route("/user_dashboard",methods=["GET","POST"])
def user_dashboard():
    if(request.method=="GET"):
        return render_template("user_dashboard.html")
    
@app.route("/user_logout",methods=["GET","POST"])
def user_logout():
    if("user_name" in session):
        if(request.method=="GET"):
            session.clear()     #destroy all user's session
            return redirect(url_for("user_login"))
    else:
        flash("You cannot access this page! Login to continue.")
        return redirect(url_for("user_login"))

    

@app.errorhandler(404)
def not_found(e):
    return "NOT FOUND"

if __name__=='__main__':
    app.run(debug=True,port=5001)