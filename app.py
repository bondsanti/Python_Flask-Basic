from pickle import FALSE
from flask import Flask, flash, redirect,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class MyForm(FlaskForm):
     name = StringField('ป้อนชื่อ', validators=[DataRequired()])
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
    form=MyForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data = ""
        # return redirect('/formwtf')
    return render_template("formwtf.html",form=form,name=name)

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     form = MyForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('formwtf.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True)
