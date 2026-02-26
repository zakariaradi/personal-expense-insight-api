from pathlib import Path
from datetime import timedelta
import os

# =========================================================
# BASE DIRECTORY
# =========================================================

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# SECURITY SETTINGS
# =========================================================

# Secret key (should be stored securely in production)
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-change-this-in-production"
)

# Debug mode (set to False in production)
DEBUG = os.getenv("DEBUG", "True") == "True"

# Allowed hosts (add your domain in production)
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost"
).split(",")

# =========================================================
# APPLICATION DEFINITION
# =========================================================

INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',

    # Local apps
    'expenses',
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Root URL configuration
ROOT_URLCONF = 'expense_api.urls'


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add custom template directories if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# WSGI application path
WSGI_APPLICATION = 'expense_api.wsgi.application'


# =========================================================
# DATABASE CONFIGURATION
# =========================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    },
]


# =========================================================
# INTERNATIONALIZATION
# =========================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =========================================================
# DJANGO REST FRAMEWORK CONFIGURATION
# =========================================================

REST_FRAMEWORK = {
    # Use JWT authentication globally
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    # Require authentication for all endpoints by default
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


# =========================================================
# SIMPLE JWT CONFIGURATION
# =========================================================

SIMPLE_JWT = {
    # Access token lifetime
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),

    # Refresh token lifetime
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),

    # Authorization header format
    'AUTH_HEADER_TYPES': ('Bearer',),
}