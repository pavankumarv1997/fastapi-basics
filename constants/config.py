import configparser

config = configparser.ConfigParser()
config.read('config\configuration.conf')

# ---------------------------SECTIONS----------------------------------
DB_SECTION = 'DB'

# ---------------------------DB----------------------------------
DB_HOST = config.get(DB_SECTION, "host")
DB_PORT = config.getint(DB_SECTION, "port")
DB_USER_NAME = config.get(DB_SECTION, "user_name")
DB_PASSWORD = config.get(DB_SECTION, "password", fallback=None)
DB_NAME = config.get(DB_SECTION, "db_name")

