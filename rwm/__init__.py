from rwm.app import app as application
from rwm.wiki import wiki

application.register_blueprint(wiki)
