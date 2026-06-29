from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-gbpn_2g45czpz+1ny2p&^lvm*xas51hge^^$v2^-n1!m=&r%b%'

DEBUG = False

ALLOWED_HOSTS = [
    ".onrender.com",
    "localhost",
    "127.0.0.1"
]


# APPLICATIONS

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # Third party
    'rest_framework',
    'corsheaders',


    # Our apps
    'users',
    'applications',
    'reviews',
    'certificates',

]


# MIDDLEWARE FIXED

MIDDLEWARE = [

'corsheaders.middleware.CorsMiddleware',

'django.middleware.security.SecurityMiddleware',

'whitenoise.middleware.WhiteNoiseMiddleware',

'django.contrib.sessions.middleware.SessionMiddleware',

'django.middleware.common.CommonMiddleware',

'django.middleware.csrf.CsrfViewMiddleware',

'django.contrib.auth.middleware.AuthenticationMiddleware',

'django.contrib.messages.middleware.MessageMiddleware',

]


CORS_ALLOW_ALL_ORIGINS = False


CORS_ALLOWED_ORIGINS = [

"http://localhost:5173",

]


# Custom user

AUTH_USER_MODEL = 'users.User'


ROOT_URLCONF = 'config.urls'


TEMPLATES = [

    {
        'BACKEND':
        'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

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


WSGI_APPLICATION = 'config.wsgi.application'


# DATABASE

DATABASES = {

    'default': {

        'ENGINE':
        'django.db.backends.sqlite3',

        'NAME':
        BASE_DIR / 'db.sqlite3',

    }

}


# PASSWORD VALIDATION

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]

REST_FRAMEWORK = {

    "DEFAULT_AUTHENTICATION_CLASSES":
    (

        "rest_framework_simplejwt.authentication.JWTAuthentication",

    )

}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True



STATIC_URL = "static/"


STATIC_ROOT = BASE_DIR / "staticfiles"


STATICFILES_STORAGE = (
"whitenoise.storage.CompressedManifestStaticFilesStorage"
)

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False
