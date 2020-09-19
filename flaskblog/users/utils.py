import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskblog import app, mail


def save_picture(form_picture):
    pict_hex_name = secrets.token_hex(8)
    _, fext = os.path.splitext(form_picture.filename)
    pict_fn = pict_hex_name+fext
    picture_path = os.path.join(app.root_path, 'static/user_profile_pics', pict_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return pict_fn



def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender = 'donotreply@demo.com', recipients = [user.email]) #why sender not donotreply@demo.com in the email?
    msg.body = f''' To reset your password, visit the following link: 
    {url_for('users.reset_token', token=token, _external=True)}

    If you did not make this request then simply ignore this email and no change will be made.
    '''
    mail.send(msg)

