# Django registration settings; One-week activation window
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/'

# Email settings for sending account activation mails
EMAIL_BACKEND = 'post_office.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "archamea.history@gmail.com"
EMAIL_HOST_PASSWORD = "Adgonoadfy97"
EMAIL_PORT = 587