from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ilovegreeneggs'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'This was removed'
app.config['MAIL_PASSWORD'] = 'This was removed'
mail = Mail(app)

from app import views