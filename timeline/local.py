SECRET_KEY = 'django-insecure-+bm9t6fwc16*730l&9ge%my7q(wj8@xcfj=h+4@t6p*@yj)z9y'
DEBUG = True
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'timeline',  # 数据库名称
        'HOST': '127.0.0.1',  # 数据库地址，本机 ip 地址 127.0.0.1
        'PORT': 3306,  # 端口
        'USER': 'timeline_admin',  # 数据库用户名
        'PASSWORD': '123456',  # 数据库密码
    }
}
