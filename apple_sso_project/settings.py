from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-apple-sso-test-key-change-in-production')

DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = ['galaluddin12.pythonanywhere.com', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'rest_framework',
    'corsheaders',
    'authentication',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'apple_sso_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'apple_sso_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8001",
    "https://galaluddin12.pythonanywhere.com",
]
CORS_ALLOW_CREDENTIALS = True


SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = True


SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['state']
SOCIAL_AUTH_IGNORE_DUPLICATE_EMAILS = True


AUTHENTICATION_BACKENDS = [
    'social_core.backends.apple.AppleIdAuth',
    'django.contrib.auth.backends.ModelBackend',
]

# Apple SSO Configuration - ALL FROM ENVIRONMENT VARIABLES
SOCIAL_AUTH_APPLE_ID_CLIENT = os.environ.get('APPLE_CLIENT_ID')
SOCIAL_AUTH_APPLE_ID_TEAM = os.environ.get('APPLE_TEAM_ID')
SOCIAL_AUTH_APPLE_ID_KEY = os.environ.get('APPLE_KEY_ID')
SOCIAL_AUTH_APPLE_ID_SECRET = os.environ.get('APPLE_PRIVATE_KEY')

SOCIAL_AUTH_APPLE_ID_SCOPE = ['email', 'name']
SOCIAL_AUTH_APPLE_ID_EMAIL_AS_USERNAME = True
SOCIAL_AUTH_APPLE_ID_CALLBACK_URL = 'https://galaluddin12.pythonanywhere.com/social-auth/complete/apple-id/'

SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'auth/welcome/'
SOCIAL_AUTH_LOGIN_ERROR_URL = 'auth/login-error/'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}