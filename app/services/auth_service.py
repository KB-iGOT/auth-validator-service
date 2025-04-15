from ..authentication.AccessTokenValidator import AccessTokenValidator

class AuthService:
    def __init__(self):
        self.access_token_validator = AccessTokenValidator()

    def is_valid_token(self, user_token):
        user_id = self.access_token_validator.verify_user_token(user_token, True)
        if (user_id == "UNAUTHORIZED"):
            return False
        return True