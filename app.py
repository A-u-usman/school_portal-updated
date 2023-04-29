from flask import Flask, render_template, url_for, request, get_flashed_messages, current_app, flash
from flaskext.mysql import MySQL
import datetime
import pymysql.cursors
import json
import os
import sqlite3
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/images'

app = Flask(__name__)
app.secret_key = 'secret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['MAX_CONTENT_LENGTH'] = 0.2 * 1024 * 1024
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DB'] = 'Students'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] ='07067Walid'


mysql = MySQL(app, cursorclass=pymysql.cursors.DictCursor)


@app.route('/')
def landingPage():

    return render_template('landingPage.html')

@app.route('/Get-started', methods=['GET', 'POST'])
def portalForm():
    if request.method=='POST':
        student_info = dict(request.form)
        passport = request.files['passport']
        firstname = student_info['firstname']
        middlename = student_info['middlename']
        lastname = student_info['lastname']
        email = student_info['email']
        dob = student_info['dob']
        gender = student_info['gender']
        phoneNumber = student_info['phoneNumber']
        address = student_info['address']
        state = student_info['state']
        lga = student_info['lga']
        nextOfKin = student_info['nextOfKin']
        jambscore = student_info['jambscore']        
        if firstname and lastname and email and dob and gender and phoneNumber and address and state and lga and nextOfKin and jambscore:
            if passport:
                filename = secure_filename(passport.filename)
                sqlite3.enable_callback_tracebacks(True)
                conn = sqlite3.connect('database.db') # mysql.get_db()
                cur = conn.cursor()
                sqlcmd = "INSERT INTO informations(firstname, middlename, lastname, email, dob, gender, phonenumber, address, soo, lga, nok, jambscore, admissionstatus, filename) VALUES(`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`)"%(firstname, middlename, lastname, email, dob,gender, phoneNumber, address, state, lga, nextOfKin, jambscore, 'undecided', filename)
                print(sqlcmd)
                cur.execute("INSERT INTO informations(firstname, middlename, lastname, email, dob, gender, phonenumber, address, soo, lga, nok, jambscore, admissionstatus, filename ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (firstname.lower(), middlename.lower(), lastname.lower(), email.lower(), dob,gender.lower(), phoneNumber, address.lower(), state.lower(), lga.lower(), nextOfKin.lower(), jambscore, 'undecided', filename))
                #"INSERT INTO informations (firstname, middlename, lastname, email, dob, gender, phonenumber, address, soo, lga, nok, jambscore, admissionstatus, filename ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (firstname, middlename, lastname, email, dob,gender, phoneNumber, address, state, lga, nextOfKin, jambscore, 'undecided', filename)
                conn.commit()
                cur.close()
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                passport.save(filepath)
                flash('Student successfully registered', 'flash_success')
                return json.dumps('success')
            else:
                flash('please upload your passport', 'flash_error')
        else:
            flash('please fill in all the necessary fields, to register a new student', 'flash_error')
    
    return render_template('portalForm.html')

@app.route('/index', methods=['POST','GET'])
def index():
    if request.method == "GET":
        conn = sqlite3.connect('database.db') #mysql.get_db()
        cur = conn.cursor()
        cur.execute('SELECT * FROM informations')
        
        rv = cur.fetchall() 
        print(rv)
        return render_template('index.html', students={'rv':rv, 'get':'get'}) 
    elif request.method == "POST":
        #student_info = dict(request.form)
        name = request.form.get('name')
        nametuple = tuple(name.split(" "))
        admissionstatus = request.form.get('admissionstatus')
        gender = request.form.get('gender')
        jambscore = request.form.get('jambScore')  

        a = '''SELECT * FROM informations WHERE '''
       # id, firstname, middlename, lastname, admissionstatus,gender,jambscore

        c=[]
        d=[]
        f=[]
        g = ""
        h = ""
        b = {'name':name.lower(), 'admissionstatus':admissionstatus.lower(),'gender':gender.lower(),
            'jambscore':jambscore}

        for i in b:
            if b[i] == '':
                pass
                #print(i,'is empty')
            else:
                if i=='name':
                    e = "(firstname in {} OR middlename in {} OR lastname in {})"
                    c.append(i)
                    if (b[i].find(" ")) == -1 :
                        n=(name.lower(),name.lower()) 
                        d.append(n)
                    else: 
                        d.append(tuple(b[i].split(' ')))
                    #print(b[i])
                    f.append(e)
                elif i == 'admissionstatus':
                    e = "admissionstatus='{}'"
                    c.append(i)
                    d.append(b[i])
                    #print(b[i])
                    f.append(e)
                elif i == 'gender':
                    e = "gender='{}'"
                    c.append(i)
                    d.append(b[i])
                    #print(b[i])
                    f.append(e)
                elif i == 'jambscore':
                    e = "jambscore={}"
                    c.append(i)
                    d.append(b[i])
                    #print(b[i])
                    f.append(e)
        
        inputlen = len(c)
        if inputlen ==1:
            g = a + " {}"
            h = g.format(f[0])
           # print(h)
            conn = sqlite3.connect('database.db') #mysql.get_db()
            cur = conn.cursor()
            if name:
                print(h)
                sql3= h.format(d[0],d[0],d[0])
                print(sql3)
                cur.execute(sql3)
                rv = cur.fetchall()
            elif jambscore:
                print(h)
                print(""+d[0])

                cur.execute(h.format(d[0]))
                #cur.execute(h, (d[0]))
                rv = cur.fetchall()
            else:
                print(h)
                print(""+d[0])

                cur.execute(h.format(d[0]))
                #cur.execute(h, (d[0]))
                rv = cur.fetchall()
            #print(rv)
            conn.commit()
            cur.close()
            #flash('Student successfully searched', 'flash_success')
            #print(c)
            #print(d)

            #print(f)
            #print(g)
            #print(h)

            return render_template('index.html', students={'rv':rv})

        elif inputlen ==2:
            g = a + " {}"*2
            h = g.format(f[0],'AND ' + f[1])
           # conn = mysql.get_db()
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            if name:
                cur.execute(h.format(d[0], d[0],d[0],d[1]))
            else:
                cur.execute(h.format(d[0],d[1]))
            rv = cur.fetchall()
            #print(rv)
            conn.commit()
            cur.close()
            #print(c)
            #print(d)

            #print(f)
            #print(g)
            #print(h)

            #flash('Student successfully searched', 'flash_success')
            return render_template('index.html', students={'rv':rv})
        elif inputlen ==3:
            g = a + " {}"*3
            h = g.format(f[0],'AND ' + f[1],  'AND ' + f[2] )
            #conn = mysql.get_db()
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            if name:
                cur.execute(h.format(d[0], d[0],d[0],d[1],d[2]))
            else:
                cur.execute(h.format(d[0],d[1],d[2]))
            rv = cur.fetchall()
            #print(rv)
            conn.commit()
            cur.close()
            #flash('Student successfully searched', 'flash_success')
            #print(c)
            #print(d)

            #print(f)
            #print(g)
            #print(h)

            return render_template('index.html', students={'rv':rv})
        elif inputlen ==4:
            g = a + " {}"*4
            h = g.format(f[0],'AND ' + f[1],  'AND ' + f[2], 'AND ' + f[2])
            #conn = mysql.get_db()
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            if name:
                cur.execute(h.format(d[0], d[0],d[0],d[1],d[2],d[3]))
            else:
                cur.execute(h.format(d[0],d[1],d[2],d[3]))
            rv = cur.fetchall()
            #print(rv)
            conn.commit()
            cur.close()
            #flash('Student successfully searched', 'flash_success')
            return render_template('index.html', students={'rv':rv})
            #print(c)
            #print(d)
            #print(f)
            #print(g)
            #print(h)

        else:
            flash('kindly enter atleast one keyword to search for student(S) record', 'flash_error')
            return render_template('index.html', students={})
        


@app.route('/student/<id>/profile', methods=['POST','GET'])
def profile(id):
    student_id = id
    conn = sqlite3.connect("database.db") #mysql.get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM informations where id=?', (student_id))
    rv = cur.fetchall()
    print(rv[0])
    return render_template('profile.html', student=rv[0])
   


@app.route('/changeadmissionstatus', methods=['POST'])
def changeStatus():
    req = request.get_json()
    status = req['status']
    id = req['id']
    if status =='value1' :
        flash('please select a valid admission status ', 'flash_error')
    else:
        conn = sqlite3.connect('database.db') #mysql.get_db()
        cur = conn.cursor()
        cur.execute('update informations set admissionstatus=? where id=?', (status, id))
        conn.commit()
        cur.close()
        flash('Admission status successfully changed!', 'flash_success')
    return json.dumps('success')


    


if __name__ == "__main__":
    app.run(debug=True)


