# CLEARDB_DATABASE_URL = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': '<schema_name>',
    #     'USER': 'root',
    #     'PASSWORD': '*****',
    #     'HOST': 'localhost',
    #     'PORT': '<port_num>',
    # }
# }

import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}