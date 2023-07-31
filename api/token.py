from jwt import encode, decode

secret_key = 'DemoSecretKey'
algorithm = 'HS256'

def generate_token(payload: dict) -> str:
    return encode(payload, secret_key, algorithm=algorithm)

def verify_token(token: str) -> bool:
    try:
        decode(token, secret_key, algorithms=[algorithm])
        return True
    except:
        return False

def parse_token(token) -> dict:
    return decode(token, secret_key, algorithms=[algorithm])
