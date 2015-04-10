"""
Django settings for airbook_server project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9tm-0p!q=8@vv9o#(ubdzx8#$v@)x445%2p+_-5l51d1z&#g*o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #rest stuff
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'rest_framework.filters',
    'rest_framework_swagger',
    
    #our apps
    'airbook_users',
    'books',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'airbook_server.urls'

WSGI_APPLICATION = 'airbook_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': os.path.join(BASE_PATH, 'db', 'db.sqlite3'),
        'NAME' : os.environ.get('AIRBOOK_DB'),
        'USER' : os.environ.get('AIRBOOK_USER'),
        'PASSWORD' : os.environ.get('AIRBOOK_PASSWORD'),
        'HOST' : 'localhost'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'static_collected'))

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(BASE_DIR, "../../airbook-web/")),
    os.path.abspath(os.path.join(BASE_DIR, "../../airbook-loader/")),
)


MEDIA_ROOT = BASE_DIR
MEDIA_URL = '/media/'



REST_FRAMEWORK = {
    'PAGINATE_BY': 25,                 # Default to 10
    'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100,             # Maximum limit allowed when using `?page_size=xxx`.
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES' : (),
    'DEFAULT_PAGINATION_SERIALIZER_CLASS': 'books.pagination.CustomPaginationSerializer',
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}


SWAGGER_SETTINGS = {
    "api_key" : "8cb06edd39379aff4baa04abd51a6e80cca3db7f",
    #"is_authenticated": True,  #
    #"is_superuser": True,  #
}