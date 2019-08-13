import jwt

secret_key = "lxlzjl"
options = {
    'verify_signature': True,
    'verify_exp': True,
    'verify_nbf': False,
    'verify_iat': True,
    'verify_aud': False
}


def jwtauth(handler_class):
    ''' Handle Tornado JWT Auth '''
    def wrap_execute(handler_execute):
        def require_auth(handler, kwargs):

            auth = handler.request.headers.get('Authorization')
            if auth:
                parts = auth.split()

                if parts[0].lower() != 'bearer':
                    handler._transforms = []
                    handler.set_status(401)
                    handler.write(
                        {"status": "B12", "msg": "invalid header authorization"})
                    handler.finish()
                elif len(parts) == 1:
                    handler._transforms = []
                    handler.set_status(401)
                    handler.write(
                        {"status": "B12", "msg": "invalid header authorization"})
                    handler.finish()
                elif len(parts) > 2:
                    handler._transforms = []
                    handler.set_status(401)
                    handler.write(
                        {"status": "B12", "msg": "invalid header authorization"})
                    handler.finish()

                token = parts[1]
                try:
                    payload = jwt.decode(token, secret_key, options=options)
                    if payload:
                        return payload
                    else:
                        raise jwt.InvalidTokenError

                except jwt.ExpiredSignatureError:
                    handler._transforms = []
                    handler.set_status(401)
                    handler.write({"status": "A12", "msg": "token expired"})
                    handler.finish()

                except jwt.InvalidTokenError:
                    handler._transforms = []
                    handler.set_status(401)
                    handler.write({"status": "B12", "msg": "invalid token"})
                    handler.finish()
            else:
                handler._transforms = []
                handler.set_status(401)
                handler.write(
                    {"status": "C12", "msg": "missing authorization"})
                handler.finish()

            return True

        def _execute(self, transforms, *args, **kwargs):

            try:
                require_auth(self, kwargs)
            except Exception:
                return False

            return handler_execute(self, transforms, *args, **kwargs)

        return _execute

    handler_class._execute = wrap_execute(handler_class._execute)
    return handler_class
