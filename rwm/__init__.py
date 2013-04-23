try:
    import uwsgi
    if uwsgi.opt.get('gevent', None):
        import gevent.monkey
        gevent.monkey.patch_all()
except ImportError:
    pass

from rwm.app import app as application
from rwm.wiki import wiki

application.register_blueprint(wiki)
