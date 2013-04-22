from urllib import urlopen
from flaskex import Blueprint

wiki = Blueprint('wiki', __name__)


@wiki.route('/')
def index():
    return 'Rigveda Wiki Mirror'


@wiki.route('/wiki/<path:document>')
def page(document):
    return \
        urlopen(
            "http://www.rigvedawiki.net/r1/wiki.php/%s?action=raw" % document
        ).read()
