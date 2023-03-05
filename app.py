from flask import Flask,redirect, render_template
from flask import request
import forms 
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

app=Flask (__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.route("/",methods=['GET','POST'])
def index():
    create_forms=forms.UseForm(request.form)
    if request.method=='POST':
        alumn= Alumnos(nombre=create_forms.nombre.data,
                       apellidos=create_forms.apellidos.data,
                       email=create_forms.email.data)
        db.session.add(alumn)
        db.session.commit()
    return render_template('index.html',form=create_forms)

if __name__=='__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)