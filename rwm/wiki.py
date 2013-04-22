from flaskex import Blueprint

wiki = Blueprint('wiki', __name__)


@wiki.route('/')
def index():
    return 'Rigveda Wiki Mirror'
