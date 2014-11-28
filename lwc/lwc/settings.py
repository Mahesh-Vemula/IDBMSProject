"""
Django settings for lwc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't&6-lbzo=dx^s(8%j0(xmu(y-hl!(p%1wq9!9x2t@#0duk8k*!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'joins',
    'movietickets',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lwc.urls'

WSGI_APPLICATION = 'lwc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Parse database configuration from SDATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    #BASE_DIR + "\\templates\\"
    #'C:\\Users\\\Nandu\\Desktop\\lwc\\src\\templates\\',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static','static_root')
#STATIC_ROOT = 'C:\\Users\\\Nandu\\Desktop\\lwc\\src\\static\\static_root\\'
#print os.path.join(BASE_DIR, 'static','static_dirs')
STATICFILES_DIRS=(
    os.path.join(BASE_DIR, 'static','static_dirs'),
    os.path.join(BASE_DIR, 'templates','frontpage_files'),
    #"C:\\Users\\\Nandu\\Desktop\\lwc\\src\\static\\static_dirs\\",
    #'C:\\Users\\\Nandu\\Desktop\\lwc\\src\\templates\\frontpage_files\\',

)

MEDIA_ROOT = os.path.join(BASE_DIR, 'static','media')

MEDIA_URL = "/media/"
