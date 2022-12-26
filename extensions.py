from ast import Mod
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security
from app import app

db = SQLAlchemy(app)

from flask_login import LoginManager


migrate = Migrate(app, db)
login_manager = LoginManager(app) 
admin = Admin(app, template_mode='bootstrap3')
from models import News, Role, User, LoanRequest, CardRequest, Cards, Loans

admin.add_view(ModelView(News, db.session))

admin.add_view(ModelView(LoanRequest, db.session))
admin.add_view(ModelView(CardRequest, db.session))
admin.add_view(ModelView(Cards, db.session))
admin.add_view(ModelView(Loans, db.session))



# Flask_security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)