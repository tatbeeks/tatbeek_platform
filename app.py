from asyncio.windows_events import NULL
from flask import Flask, render_template, redirect, url_for,request
import mysql.connector
from sqlalchemy import null 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="tatbeekdb"
)
mycursor = mydb.cursor()
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def insert_role():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        name = request.form['role']
        sql = "INSERT INTO role(role_id,role_name) VALUES (%s,%s)"
        val = (NULL,name)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('success.html')
 

app.run(host='localhost', port=7000)