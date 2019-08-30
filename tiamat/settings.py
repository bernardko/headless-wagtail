"""
Django settings for tiamat project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os

from configurations import Configuration, values


class Common(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = values.ListValue([])

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'whitenoise.runserver_nostatic',
        'django.contrib.staticfiles',
        'django.contrib.humanize',
        "django.contrib.sitemaps",

        'wagtail.contrib.forms',
        'wagtail.contrib.redirects',
        'wagtail.embeds',
        'wagtail.sites',
        'wagtail.users',
        'wagtail.snippets',
        'wagtail.documents',
        'wagtail.images',
        'wagtail.search',
        'wagtail.admin',
        'wagtail.core',

        'modelcluster',
        'taggit',

        'django_extensions',
        'debug_toolbar',
        'corsheaders',
        'headlesspreview',
        'graphene_django',

        'tiamat.users',
        'tiamat.core',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',

        'wagtail.core.middleware.SiteMiddleware',
        'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    ]

    ROOT_URLCONF = 'tiamat.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
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

    WSGI_APPLICATION = 'tiamat.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/2.2/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(
        'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
    )

    # Password validation
    # https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
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
    # https://docs.djangoproject.com/en/2.2/topics/i18n/
    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.2/howto/static-files/
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    MEDIA_PREFIX = "http://artoria:8001"
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = values.Value('/media/')

    AUTH_USER_MODEL = 'users.User'

    WAGTAIL_SITE_NAME = 'Tiamat'
    WAGTAILIMAGES_IMAGE_MODEL = 'core.CoreImage'

    GRAPHENE = {
        'SCHEMA': 'tiamat.graphql.schema.schema'
    }

    PREVIEW_URL = values.Value(environ_name="PREVIEW_URL")

    CORS_URLS_REGEX = r'^(\/graphql\/.*)$'


class Development(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    ALLOWED_HOSTS = ['*']

    INTERNAL_IPS = [
        '127.0.0.1'
    ]

    MIDDLEWARE = Common.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]

    CORS_ORIGIN_ALLOW_ALL = True


class Staging(Common):
    """
    The in-staging settings.
    """
    # Security
    # SESSION_COOKIE_SECURE = values.BooleanValue(True)
    # SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    # SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    # SECURE_HSTS_SECONDS = values.IntegerValue(31536000)
    # SECURE_REDIRECT_EXEMPT = values.ListValue([])
    # SECURE_SSL_HOST = values.Value(None)
    # SECURE_SSL_REDIRECT = values.BooleanValue(True)
    # SECURE_PROXY_SSL_HEADER = values.TupleValue(
    #     ('HTTP_X_FORWARDED_PROTO', 'https')
    # )

    ALLOWED_HOSTS = ['*']

    MEDIA_PREFIX = "http://artoria:8002"
    CORS_ORIGIN_ALLOW_ALL = True


class Production(Staging):
    """
    The in-production settings.
    """
    pass
