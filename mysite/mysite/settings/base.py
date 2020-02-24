from os.path import join, abspath, dirname
here = lambda *dirs: join(abspath(dirname('.')), *dirs)
BASE_DIR = here('..', '..')
root = lambda *dirs: join(abspath(BASE_DIR), *dirs)

# MEDIA_ROOT 설정
MEDIA_ROOT = root('media')

# STATIC_ROOT 설정
STATIC_ROOT = root('collected_static')

# 정적파일의 추가위치
STATICFILES_DIRS = (
    root('assets'),
)

# TEMPLATE_DIRS 설정
TEMPLATES = [
    {
        'BACKEND' : 'jdango.template.backends.django.djangotemplates',
        'DIRS' : (root('temp[lates')) ,
        )
    }
]