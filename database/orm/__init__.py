from .ebook import EbookORM
from .user import UserORM

ORM = {
    'User': UserORM(),
    'Ebook': EbookORM()
}