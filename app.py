from flask import Flask

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/yelo-bank'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '123'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECURITY_PASSWORD_SALT'] = 'kerim123'
app.config['SECURITY_PASSWORD_HASH'] = 'sha512_crypt'



from extensions import *
from controllers import *
from models import *
from forms import *


# Run
if __name__ == '__main__':
    app.init_app(db)
    app.init_app(migrate)
    app.run(port=5000, debug = True)

