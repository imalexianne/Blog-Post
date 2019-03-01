from app import create_app,db
from app.models import User,Blogpost,Comment
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
# from flask_login import LoginManager

# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'


# Creating app instance
app = create_app('development')
app = create_app('test')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Blogpost=Blogpost,Comment=Comment )
if __name__ == '__main__':
    manager.run()