from flask.ext.wtf import Form, TextField, PasswordField, Required, Email

class LoginForm(Form):
    email = TextField('Email', [Required(), Email()])
    password = PasswordField('Password', [Required()])