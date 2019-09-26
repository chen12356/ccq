from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app
from App.views import blue

app  = create_app('develop')
app.register_blueprint(blueprint=blue)
manager = Manager(app=app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()