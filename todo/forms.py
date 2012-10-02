from flask.ext.wtf import Form, TextField, PasswordField, Required, Email

class LoginForm(Form):
    email = TextField('Email', [Required(message='Este campo es requerido'), Email(message='E-mail no valido')])
    password = PasswordField('Password', [Required(message='Este campo es requerido')])