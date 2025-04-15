import os

SUNBIRD_SSO_URL = os.environ.get('SUNBIRD_SSO_URL', 'https://portal.dev.karmayogibharat.net/auth/')
SUNBIRD_SSO_REALM = os.environ.get('SUNBIRD_SSO_REALM', 'sunbird')
ACCESS_TOKEN_PUBLICKEY_BASEPATH = os.environ.get('accesstoken_publickey_basepath')
X_AUTHENTICATED_USER_TOKEN = 'x-authenticated-user-token'