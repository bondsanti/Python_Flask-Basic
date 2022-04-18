from pickle import FALSE
from flask import Flask, flash, redirect,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,RadioField,SelectField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
Bootstrap(app)

class MyForm(FlaskForm):
     name = StringField('ป้อนชื่อ', validators=[DataRequired()])
     gender = RadioField('เพศ',choices=[('male','ชาย'),('female','หญิง')],validators=[DataRequired()])
     exp = SelectField('ประสบการณ์ทำงาน',choices=[('น้อยกว่า 2 ปี','น้อยกว่า 2 ปี'),('มากกว่า 2 ปี','มากกว่า 2 ปี'),('ไม่มีประสบการณ์','ไม่มีประสบการณ์')],validators=[DataRequired()])
     checkAccept = BooleanField('ยอมรับข้อมูลว่าที่กรอกมาเป็นความจริง')
     submit = SubmitField("บันทึกข้อมูล")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form1')
def form1():
    return render_template("formstd.html")

# @app.route('/user/<name>/<age>')
# def user(name,age):
#     return "สวัสดี : คุณ {} อายุ : {} ".format(name,age)
@app.route('/sendData')
def contactForm():
    emailcontact = request.args.get('emailcontact')
    namecontact = request.args.get('namecontact')
    detail = request.args.get('detail')
    data = {emailcontact,namecontact,detail}
    return render_template("formstd.html",mydata = data)
     

@app.route('/form2',methods=['GET', 'POST'])
def form2():
    name=False
    checkAccept=False
    gender=False
    exp=False
    form=MyForm()
    if form.validate_on_submit():
        flash("สำเร็จ..!!")
        name=form.name.data
        checkAccept=form.checkAccept.data
        gender=form.gender.data
        exp=form.exp.data
        #เคลียร์ค่าจากฟอร์ม
        form.name.data = ""
        form.checkAccept.data = ""
        form.gender.data = ""
        form.exp.data = ""
        # return redirect('/formwtf')
    return render_template("formwtf.html",form=form,name=name,checkAccept=checkAccept,gender=gender,exp=exp)

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     form = MyForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('formwtf.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True)
