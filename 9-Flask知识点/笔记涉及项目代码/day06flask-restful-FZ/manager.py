from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

app  = create_app('develop')
# 解决中文乱码
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

manager = Manager(app=app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()