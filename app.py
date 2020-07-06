import os

from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD'],
    "CLIENT_MAIL": os.environ['CLIENT_EMAIL']
}

app.config.update(mail_settings)
mail = Mail(app)


@app.route('/send-mail/', methods=['GET'])
def process():
    name = request.args['name']
    email = request.args['email']
    msg = Message(subject=f"New Subscriber {name}",
                  sender=app.config.get("MAIL_USERNAME"),
                  recipients=[app.config.get("CLIENT_MAIL")],
                  body=f"email: {email}")
    mail.send(msg)

    return {"status": True, "message": "success"}


if __name__ == '__main__':
    app.run(port=5000)
