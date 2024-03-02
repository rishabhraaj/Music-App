import mysql.connector
from flask import session

class UserOperation:
    def connection(self):
        con=mysql.connector.connect(host="localhost",port="3306",user="root",password="Rish@880abh",database="cloud_beats")
        return con
    
    def user_insert(self,fname,lname,email,user_name,password):
        db = self.connection()
        mycursor = db.cursor()

        sq = "insert into user (fname,lname,email,user_name,password) values (%s,%s,%s,%s,%s)"

        record=[fname,lname,email,user_name,password]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return
    
    def user_check(self,user_name):
        db = self.connection()
        mycursor = db.cursor()
        sq ="select user_name from user where user_name=%s"

        record=[user_name]
        mycursor.execute(sq,record)
        mycursor.fetchall()
        rc=mycursor.rowcount
        if(rc==0):
            return 0
        else:
            return 1

    def email_check(self,email):
        db = self.connection()
        mycursor = db.cursor()
        sq ="select email from user where email=%s"

        record=[email]
        mycursor.execute(sq,record)
        mycursor.fetchall()
        rc=mycursor.rowcount
        if(rc==0):
            return 0
        else:
            return 1
        

    def user_delete(self,email):
        db = self.connection()
        mycursor = db.cursor()
        sq = "delete from user where email=%s"
        record=[email]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return
    

    def user_login(self,user_name,password):
        db=self.connection()
        mycursor=db.cursor()
        sq="select fname,user_name from user where user_name=%s and password=%s"
        record=[user_name,password]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        rc=mycursor.rowcount

        mycursor.close()
        db.close()

        if(rc==0):
            return 0
        else:
            session["user_fname"]=row[0][0]
            session["user_name"]=row[0][1]
            return 1
        

        