from flask_script import Manager, Shell
from flask_migrate import MigrateCommand
from app import create_app
from app import models
from app import db

def _make_context():
    return dict(app=create_app, db=db, models=models)

manager = Manager(create_app)
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=_make_context))

manager.run()