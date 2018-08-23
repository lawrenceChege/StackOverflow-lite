from api.app import APP
from migrations import create_tables

create_tables()

if __name__ == '__main__':
    APP.run(debug=True)