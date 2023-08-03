from api import Rule
from api.api import Api
from database.orm import ORM
from flask import Blueprint

ebook = Blueprint('Ebook', __name__, url_prefix = '/ebook')

EbookRule = Rule['Ebook']
EbookORM = ORM['Ebook']

@ebook.route('/upload', methods = ['POST'])
@Api.use(EbookRule['Upload'])
def upload(remote_url, name, description, token):
    if EbookORM.upload(token['userid'], remote_url, name, description):
        return 'ok'
