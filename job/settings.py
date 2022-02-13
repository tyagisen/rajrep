

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'etdq)uvq=t0rc&ams5_ovn6w8bcwknjj0u97*(#n^(76x*+dr1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',

    'jobapp.apps.JobappConfig',
    'account.apps.AccountConfig',
    'letter.apps.LetterConfig',
    #3rd Party App
    'ckeditor',
    'taggit',
    'user_visit',
    'crispy_forms',
    'ckeditor_uploader',
    
    'tinymce',
    'social_django',
    'posts',
]


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':[ ['CodeSnippet', ], ],
        'height': 400,
        'width': 900,
        'removePlugins': 'stylesheetparser',
        'extraPlugins': 'codesnippet',
   },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'user_visit.middleware.UserVisitMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'job.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


WSGI_APPLICATION = 'job.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'The JobHub',
#         'USER': 'postgres',
#         'PASSWORD': 'asusrog123',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}




# Password validation


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

AUTH_USER_MODEL = 'account.User'

# CKeditor Config
CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'tabSpaces': 4,

    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rijanchauhan03@gmail.com'
EMAIL_HOST_PASSWORD = 'saya5455687@1'
EMAIL_PORT = 587


from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

# Activate Django-Heroku.

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

SOCIAL_AUTH_FACEBOOK_KEY = '439179394496905'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '9b8120f20bf03905555bce13a08fa1ce'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '416396897780-qjkh4r83tfgqqonkho5f2bin0vs4ogvh.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'



TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}

MAILCHIMP_API_KEY = ''
MAILCHIMP_DATA_CENTER = ''
MAILCHIMP_EMAIL_LIST_ID = ''



# ckeditor 
# run python manage.py collect static to collect static file
CKEDITOR_UPLOAD_PATH = "uploads/" # ckeditor file upload paths
CKEDITOR_RESTRICT_BY_USER = True # shows file uploaded by respective user only
CKEDITOR_ALLOW_NONIMAGE_FILES = False # allows to upload image only
CKEDITOR_BROWSE_SHOW_DIRS = True # shows image by dirs
CKEDITOR_RESTRICT_BY_DATE = True # shows image by date
CKEDITOR_IMAGE_BACKEND = "pillow" # for thumbnail generation
# run python manage.py generateckeditorthumbnails to generate thumbnails

# ckeditor configuration 
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 450,
        'width': 900,
        
    },
}