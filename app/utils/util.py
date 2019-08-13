
import jwt

# check token
def decode_auth_token(auth_token):

    try:
        payload = jwt.decode(auth_token, config.SECRET_KEY, options={'verify_exp': False})
        if payload:
            return payload
        else:
            raise jwt.InvalidTokenError

    except jwt.ExpiredSignatureError:
        return 'token expired'

    except jwt.InvalidTokenError:
        return 'invalid Token'


def gen_auth_token():
    # token = jwt.encode(playload, "wechat", algorithm='HS256').decode('ascii')
    encoded_jwt = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')