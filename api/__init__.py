from .api import Api
from .user import UserRule
from .token import generate_token, verify_token, parse_token

Rule = {
    'User': UserRule
}