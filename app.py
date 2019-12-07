from flask import Flask, redirect
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "D1n@s@y@ng"

ENV = 'prod'

if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost:5000/worker'
    app.debug = True
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ougnrugttymzmj' \
                                            ':fa0206554316f9af88305ab67ee3ce4c0df86bb663d8f8048187510738955ac3@' \
                                            'ec2-174-129-255-72.compute-1.amazonaws.com:5432/dctlbiti5t1jfh'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class EmployeeModel(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(100))
    address = db.Column(db.String(500))
    phone = db.Column(db.String(20))

    def __init__(self, name, email, address, phone):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone


@app.route('/')
def index():
    data = db.session.query(EmployeeModel).all()
    print(data)
    return render_template('home.html', data=data)


@app.route('/add_employee/', methods=["POST"])
def add_employee():
    nama = request.form['add_name']
    email = request.form['add_email']
    address = request.form['add_address']
    phone = request.form['add_phone']
    print(nama + email + address + phone)
    if db.session.query(EmployeeModel).filter(EmployeeModel.name == nama).count() == 0:
        data = EmployeeModel(nama, email, address, phone)
        db.session.add(data)
        db.session.commit()
        return redirect("/")


@app.route('/delete_employee/', methods=["POST"])
def delete_employee():
    delete_id = request.form['delete_id']
    delete_item = db.session.query(EmployeeModel).filter_by(id=delete_id).first()
    db.session.delete(delete_item)
    db.session.commit()
    return redirect("/")


@app.route('/edit_employee/', methods=['POST'])
def edit_employee():
    edit_id = request.form['edit_id']
    edit_item = db.session.query(EmployeeModel).filter_by(id=edit_id).first()
    edit_item.name = request.form['edit_name']
    edit_item.email = request.form['edit_email']
    edit_item.address = request.form['edit_address']
    edit_item.phone = request.form['edit_phone']
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(port=8000)
