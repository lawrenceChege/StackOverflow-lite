import os
from api.app import APP
from instance.config import app_config
from migrations import create_tables

APP.config.from_object(app_config[os.getenv('APP_SETTINGS')])
create_tables()

if __name__ == '__main__':
    APP.run(debug=True)