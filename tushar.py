from flask import Flask,render_template, request
from flask_wtf import Form

from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)



## here we define a web form --> in flask
class NameForm(Form):
    firstname=StringField(validators=[DataRequired()])
    lastname=StringField(validators=[DataRequired()])
    submit=SubmitField()

@app.route('/webforms',methods=['GET',"POST"])
def webforms():
    NF=NameForm()

    if request.method=='POST':
        form_data=NameForm(request.form)

        if form_data.validate():
            # return form_data.firstname.data     ## for specific data
            return form_data.data
        

    return render_template('webforms.html',NF=NF)








## here we define a normal form
@app.route('/htmlforms',methods=['GET','POST'])
def htmlforms():
    if request.method=='POST':
        fd=request.form
        return str(fd)
    return render_template('htmlforms.html')



if __name__ == '__main__':
    app.run(debug=True)