from .user import UserORM, UserConnection

ORM = {
    'User': UserORM(UserConnection())
}