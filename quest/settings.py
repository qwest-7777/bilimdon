
import os
import django.conf.locale
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vxl%69e@pexrx2%%#cam^g8yq2=d1+od+m73)8-!%7l69-qb0h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'question.apps.QuestionConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'click.apps.ClickConfig',
    'payments',
    'pinax.referrals',
    'django.contrib.sites',
]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pinax.referrals.middleware.SessionJumpingMiddleware',

]

ROOT_URLCONF = 'quest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'quest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'uz-UZ'

LANGUAGES = [
	('ru', _("Русский")),
	('uz', _("O'zbekcha")),
]

LANGUAGE_COOKIE_NAME = 'lang'

LOCALE_PATHS = (
	os.path.join(BASE_DIR, 'locale'),
)

LANG_INFO = django.conf.locale.LANG_INFO.copy()


TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 
AUTH_USER_MODEL = 'question.CustomUser'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
# 
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# 

PAYMENT_HOST = '127.0.0.1:8000'
PAYMENT_USES_SSL = False # set the True value if you are using the SSL
PAYMENT_MODEL = 'question.Payment' 
# payment model format like this :: '<app_name>.<model_name>'
# add "click" to your variants
PAYMENT_VARIANTS = {
    
    'click' : ('click.ClickProvider', {
        'merchant_id' : 1111,
        'merchant_service_id' : 11111,
        'merchant_user_id' : 11111,
        'secret_key' : 'AAAAAA'
    })
    
}

