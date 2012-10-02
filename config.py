__author__ = 'gbaldera'

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#configuraciones
DEBUG = False
SECRET_KEY = 'e388079274a17ea64c5e685397c58f21'

#db
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'todo.db')

#forms
CSRF_ENABLED = True
CSRF_SESSION_KEY = "124bb2eaaec459e85d47027786fa732f"
