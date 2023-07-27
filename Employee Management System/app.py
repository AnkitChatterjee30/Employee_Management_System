from flask import Flask, request, render_template, session, redirect, url_for

from datetime import datetime, date

app=Flask(__name__)

headings=['Name', 'Mail', 'Time In','Time Out','Total Time']
data= [
    ['Ankit', 'ankitchatterjee30@gmail.com','19:28:35','19:28:52','16.983359'],
]
headers=['Name', 'Mail','Password']
data_private= [
    ['Ankit', 'ankitchatterjee30@gmail.com','12345'],
]


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/success_register', methods=["POST","GET"])
def success_register():
    t1=datetime.now()
    name = request.form['fname']
    mail = request.form['mail']
    password = request.form['pass']
    confirm = request.form['confirm']
    for i in range(len(data)):
        if data[i][0]==name:
            return render_template("already_account.html",name=name)
        else:
            if confirm==password:
                lisg=[name, mail,password]
                t2=datetime.now()
                time_diff=t2-t1
                lips=[name, mail,t1.strftime("%H:%M:%S"),t2.strftime("%H:%M:%S"), time_diff.total_seconds()*100]
                data.append(lips)
                data_private.append(lisg)
                return render_template('success_register.html',name=name)
    return render_template("error.html")

# @app.route('')

@app.route('/login',methods=['POST','GET'])
def login():
    return render_template('login.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    return render_template('signup.html')


@app.route('/dashboard', methods=['POST','GET'])
def register():
    name = request.form['fname']
    password = request.form['pass']
    for i in range(len(data_private)):
        if data_private[i][0]==name and data_private[i][2]==password:
            return render_template('dashboard.html',name=name)
        elif data_private[i][0]==name and data_private[i][2]!=password:
            return render_template('wrong_password_login.html',name=name)
    else:
        return render_template("error_login.html")

@app.route('/employee_list')
def employees():
    return render_template("employee_list.html",data=data, headings=headings)

@app.route('/logout')
def logout():
    return render_template("index.html")


@app.route('/certificate', methods=['POST','GET'])
def certificate():
    name_certificate = request.form['name_certificate']
    task1= int(request.form['task-1'])
    task2= int(request.form['task-2'])
    task3= int(request.form['task-3'])
    task4= int(request.form['task-4'])
    task5= int(request.form['task-5'])
    if task1+task2+task3+task4+task5>=3:
        return render_template("certificate.html",name_certificate=name_certificate)
    else:
        return render_template("certificate_fail.html",name_certificate=name_certificate)
@app.route('/appointment',methods=['POST','GET'])
def appoint():
    today_date= date.today().strftime("%d/%m/%y")
    name_certificate = request.form['name_certificate']
    return render_template("appointment_letter.html",name_certificate=name_certificate,today_date=today_date)

if __name__=='__main__':
    app.run(debug=True)