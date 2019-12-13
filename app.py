from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
ENV = 'prod'


def create_app():
    app.config['SECRET_KEY'] = "31aAqw11az4z7xa4qw21etE"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if ENV == 'dev':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost:5000/worker'
        app.debug = True
    else:
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ougnrugttymzmj' \
                                                ':fa0206554316f9af88305ab67ee3ce4c0df86bb663d8f8048187510738955ac3@' \
                                                'ec2-174-129-255-72.compute-1.amazonaws.com:5432/dctlbiti5t1jfh'

    db.init_app(app)

    # Blueprint
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    print("HALLO")
    if __name__ == "__main__":
        app.run(port="8000")

    return app


create_app()
